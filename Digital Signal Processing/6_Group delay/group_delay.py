"""
Created on Sat Aplil 17 2021
From:
https://dspillustrations.com/pages/posts/misc/group-delay-and-phase-delay-example.html
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

f0 = 1e4     # The resonant frequency of the circuit
f1 = 5e3     # A second test frequency we are going to use below
alpha = 5000 # the damping factor
C = 1e-6     # define the capacitor value

# calculate the other parts of the circuit
L = 1/((2*np.pi*f0)**2*C)
R = 2*alpha*L

print ("R=%.2f Ohm" % R)
print ("L=%.2e Henry" % L)
print ("C=%.2e Farad" % C)

system = signal.TransferFunction([R*C, 0], [L*C, R*C, 1])

# the sampling frequency to simulate the time-continuous system in discrete time
Fs = 1e6
T = np.arange(0, 1e-3, 1/Fs)
t, h = signal.impulse2(system, T=T)

plt.figure(figsize=(8,4))
plt.plot(t*1000, h, 'navy')
plt.grid(True)
plt.xlabel('$t$ [ms]')
plt.ylabel('$h(t)$');
plt.title('Impulse response of RLC circuit')
# plt.savefig('1_Impulse response of RLC circuit.png', dpi=600) 
plt.show()


# calculte frequency response
w, H = signal.freqresp(system, 2*np.pi*np.logspace(0, 6, 10000))
# find indices for both test frequencies and evaluate the amplitude
indf0 = np.argmin(abs(w-2*np.pi*f0))
indf1 = np.argmin(abs(w-2*np.pi*f1))
H0 = abs(H[indf0])
H1 = abs(H[indf1])

plt.figure(figsize=(8,3))
plt.subplot(121) 
plt.semilogx(w/(2*np.pi), 20*np.log10(abs(H)), 'navy')
plt.grid(True)
plt.ylim((-40, 2))
plt.xlim((1e3, 1e5))
plt.axvline(f0, color='r', ls='dashed')
plt.axvline(f1, color='navy', ls='dashed')
plt.axhline(20*np.log10(H0), color='r', ls='dashed')
plt.axhline(20*np.log10(H1), color='navy', ls='dashed')
plt.ylabel('$|H(f)|$'); plt.xlabel('$f$ [Hz]');

plt.subplot(122)
plt.semilogx(w/(2*np.pi), np.angle(H), 'navy')
plt.grid(True)
plt.xlim((1e3, 1e5))
plt.ylabel(r'$\angle H(f)$'); plt.xlabel('$f$ [Hz]')
plt.tight_layout()  
plt.show()

print ("H(f0)=%.1fdB" % (20*np.log10(H0)))
print ("H(f1)=%.1fdB" % (20*np.log10(H1)))


from sympy import symbols
from sympy import init_printing
init_printing()
R_, L_, C_, s_, z_, T_ = symbols('R L C s z T')

Hs = (s_*R_*C_)/(s_**2*L_*C_+s_*R_*C_+1)
print ("H(s)=", Hs)

Hz = Hs.copy().subs(s_, 2/T_*(z_-1)/(z_+1))
print ("H(z)=", Hz.cancel().collect(z_))

systemD = signal.cont2discrete((system.num, system.den), 1/Fs, method='bilinear')
systemD = (systemD[0][0], systemD[1], systemD[2])

plt.figure(figsize=(8,3))
plt.subplot(121)
w=2*np.pi*np.linspace(100, 2e4, 50000)/Fs
_, gd = signal.group_delay(systemD[:2], w=w)  # calculate group delay
_, H = signal.dfreqresp(systemD, w=w)  # calculate frequency response

# calculate phase and group delay at the specific frequencies
indf0 = np.argmin(abs(w - 2*np.pi*f0/Fs))
indf1 = np.argmin(abs(w - 2*np.pi*f1/Fs))
tau_gf0 = gd[indf0]*1000/Fs
tau_gf1 = gd[indf1]*1000/Fs
tau_phif0 = (-np.angle(H[indf0])/w[indf0] /Fs*1000)
tau_phif1 = (-np.angle(H[indf1])/w[indf1] /Fs*1000)

plt.plot(w/(2*np.pi)*Fs, gd/Fs*1000, 'navy')
plt.grid(True); plt.xlabel('$f$ [Hz]')
plt.ylabel(r'$\tau_g$ [ms]')
plt.title("Group Delay")
plt.axhline(tau_gf0, color='r', ls='dashed')
plt.axvline(f0, color='r', ls='dashed')

plt.subplot(122)
plt.semilogy(w/(2*np.pi)*Fs, abs(np.angle(H)/w /Fs*1000), 'navy')
plt.grid(True)
plt.xlim((1e3, 2e4))
plt.xlabel('$f$ [Hz]'); plt.ylabel(r'$\tau_\phi$ [ms]')
plt.title('Phase Delay')
plt.axhline(abs(tau_phif1), color='navy', ls='dashed')
plt.axvline(f1, color='navy', ls='dashed')
plt.tight_layout() 
plt.show()

print ("tau_g(f0)=%.2fms" % (tau_gf0))
print ("tau_phi(f0)=%.3fms" % tau_phif0)
print ("tau_g(f1)=%.2fms" % tau_gf1)
print ("tau_phi(f1)=%.3fms" % tau_phif1)

T = 1e-2
t = np.arange(0, T, 1/Fs)
envelope = np.exp(-5e5*(t-T/2)**2)

sig1 = envelope * np.sin(2*np.pi*f0*t)
sig2 = envelope * np.sin(2*np.pi*f1*t)
plt.figure(figsize=(8,3))
plt.plot(t*1000, sig1, 'lightsalmon', label='Signal $x(t)$')
plt.plot(t*1000, envelope, 'firebrick', label='Envelope')
plt.xlabel('$t$ [ms]')
plt.ylabel('$x(t)$')
plt.grid(True)
plt.legend()
plt.show()


out1 = signal.dlsim(systemD, sig1)[1]
out2 = signal.dlsim(systemD, sig2)[1]


# Just some helper function for nicer frequency formatting
def toKilo(f):
    if f % 1000 == 0:
        return "%dk" % (f//1000)
    else:
        return ("%.1fk" % (f/1000))


def plotInputOutput():
    plt.figure(figsize=(8,3))
    plt.subplot(121)
    plt.plot(t*1000, out1, 'b-', label='Output $y(t)$')
    plt.plot(t*1000, sig1, 'r-', label='Input $x(t)$')
    plt.plot(1000*t+.2, envelope*out1.max(), 'b-', lw=2)
    plt.plot(t*1000, envelope, 'r-', lw=2)
    plt.title(r'$f_0=%sHz$: $\tau_g=%.2fms,\tau_\phi=%.3fms$' % (toKilo(f0), tau_gf0, tau_phif0));
    plt.xlabel('$t$ [ms]'); plt.ylabel('$x(t)$');
    plt.xlim((1000*T/2-3, 1000*T/2+3))
    plt.ylim((-1.1, 1.1))
    plt.grid(True)
    plt.legend(fontsize=10, loc='lower right')

    plt.subplot(122)
    plt.plot(t*1000, out2, 'b-', label='Output $y(t)$')
    plt.plot(t*1000, sig2, 'r-', label='Input $x(t)$')
    plt.plot(t*1000, envelope*out2.max(), 'b-', lw=2)
    plt.plot(t*1000, envelope, 'r-', lw=2)
    plt.xlim((1000*T/2-3, 1000*T/2+3))
    plt.ylim((-1.1,1.1))
    plt.title(r'$f_0=%sHz$: $\tau_g=%.2fms, \tau_\phi=%.3fms$' % (toKilo(f1), tau_gf1, tau_phif1));
    plt.xlabel('$t$ [ms]')
    plt.ylabel('$x(t)$')
    plt.grid(True)
    plt.legend(fontsize=10, loc='lower right');
    plt.tight_layout()
plotInputOutput()

plotInputOutput()
plt.subplot(121)
plt.xlim((4.8, 5.5))
plt.ylim((H0-0.1, 1.05))
plt.annotate(s='',xy=(5,1.02), xytext=(5 + tau_gf0,1.02), arrowprops=dict(arrowstyle='<->'))
plt.text(5+tau_gf0/2,1.02,r'$\tau_g$',va='bottom', ha='center', fontsize=12)
plt.axvline(5,color='r')
plt.axvline(5.2, color='b')

plt.subplot(122)
plt.xlim((4.95, 5.1))
t0 = (np.round(f1*5.05/1000)+0.25) / f1 * 1000  # find time of peak of input curve around time=5.05ms
plt.axvline(t0, color='r')
plt.axvline(t0+tau_phif1, color='b')
plt.ylim((H1-0.2, 1.15))
plt.legend(loc='upper left', fontsize=10)
plt.annotate(s='',xy=(t0+tau_phif1,0.4), xytext=(t0,0.4), arrowprops=dict(arrowstyle='<->'))
plt.text(t0+tau_phif1/2,0.4,r'$\tau_\phi$',va='bottom', ha='center', fontsize=12) 
plt.show()