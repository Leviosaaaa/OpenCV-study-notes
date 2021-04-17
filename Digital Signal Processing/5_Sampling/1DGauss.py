import numpy as np
from numpy.fft import fft, fftshift
import matplotlib.pyplot as plt


def Gauss(sigma, mu, x):
    return np.exp((-(x - mu)**2) / (2.*(sigma**2)))

def FFT(x):
    t = np.linspace(-5, 5, num=5000)
    x = Gauss(2, 0, t)
    x_fft = fft(x)
    fh = np.where(abs(x_fft) < 1e-5)
    print("fh =", fh[0][0] / len(x))
    # f = np.arange(len(x_fft)) - len(x_fft)/2  
    # plt.plot(f, np.abs(x_fft))
    # plt.show()
    return fh[0][0] / len(x)

def interpolate(x, n0, fs):
    # Conv x*sinc to reconstruction the analog signal 
    # fs = 0.9
    x_re = np.zeros(1000)
    t = np.linspace(-5, 5, num=1000)
    n = np.linspace(-5*fs, 5*fs, num=10)
    
    for i in range(len(x)):   
        i_ = np.ones(1000) * n[i] / fs
        x_re += Gauss(2, 0, n[i] / fs) * np.sinc(fs*(t - i_))
        plt.plot(t, Gauss(2, 0, n[i] / fs) * np.sinc(fs*(t - i_)), 'lightsalmon', linewidth=0.8)

    plt.plot(t, x_re, 'r')
    plt.scatter(n0, x, s=18, c='firebrick')
    plt.title("Reconstruction by adding modulated sinc ")
    plt.savefig('add_sinc.png', dpi=600)    
    plt.show()

    return x_re

def compute_error(x, x_re):
    return np.mean(np.abs(x - x_re))

def plot(x, t, x_sa, n, x_re):
    ax1 = plt.subplot(311)
    ax1.set_title("Continuous Gauss signal")
    plt.plot(t, x, 'navy')
    plt.ylabel('x(t)')
    plt.xlabel('t')

    ax2 = plt.subplot(312)
    ax2.set_title("Sampled signal")
    plt.scatter(n, x_sa, s=12, c='firebrick')
    plt.ylabel('x[n]')
    plt.xlabel('n')

    ax3 = plt.subplot(313)
    ax3.set_title("Interpolated signal")
    plt.plot(t, x_re, 'r')
    plt.ylabel('x_re(t)')
    plt.xlabel('t')

    plt.tight_layout() 
    plt.show()


if __name__ == "__main__":
    t = np.linspace(-5, 5, num=1000)
    x = Gauss(2, 0, t)
    fh = FFT(x)

    sa_f = 10
    n = np.linspace(-5, 5, num=sa_f)
    x_sa = Gauss(2, 0, n)

    x_re = interpolate(x_sa, n, 2.05*fh)

    print("error =", compute_error(x, x_re))
    plot(x, t, x_sa, n, x_re)
