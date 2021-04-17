import cmath
import numpy as np
import matplotlib.pyplot as plt

f = lambda t : t * (np.heaviside(t + 1, 0) - np.heaviside(t, 0)) + 1

def pad(inputList):
   k = 0
   while 2**k < len(inputList):
      k += 1
   return np.concatenate((inputList, ([0] * (2**k - len(inputList)))))

def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

def fft(signal):
   n = len(signal)
   if n == 1:
      return signal
   else:
      Feven = fft([signal[i] for i in range(0, n, 2)])
      Fodd = fft([signal[i] for i in range(1, n, 2)])
 
      combined = [0] * n
      for m in range(n//2):
         combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
         combined[m + n//2] = Feven[m] - omega(n, -m) * Fodd[m]

   return np.array(combined)

def ifft(signal):
   timeSignal = fft([x.conjugate() for x in signal])
   return [x.conjugate()/len(signal) for x in timeSignal]

def np_gt(signal):
   ft_Signal = np.fft.fft(signal)
   ift_Signal = np.fft.ifft(ft_Signal)
   return ft_Signal, ift_Signal


if __name__ == "__main__":
   t = np.arange(-1, 0, 0.001) 
   temp = f(t) - 0.5
   x = np.tile(temp, 6)

   x_pad = pad(x)

   F = fft(x_pad)
   F = np.array(F)
   x_ift = ifft(F)

   np_F, np_x_ift = np_gt(x)
   print(np_F.shape, np_x_ift.shape)
   # print(F)
   t_ = np.arange(len(F))


   # plt.plot(t_, abs(F), 'r')
   # plt.ylabel('F(jw)')
   # plt.xlabel('w')


   ax1 = plt.subplot(3, 1, 1) # 两行一列，位置是1的子图
   ax1.set_title("Sawtooth signal")
   plt.plot(t_, x_pad, 'r')
   plt.ylabel('x[n]')
   plt.xlabel('n')

   ax2 = plt.subplot(3, 1, 2)
   ax2.set_title("Fourier Transform")
   plt.plot(t_, abs(F), 'r')
   plt.ylabel('F(jw)')
   plt.xlabel('w')

   # ax3 = plt.subplot(3, 1, 3)
   # ax3.set_title("Inverse Fourier Transform")
   # plt.plot(t_, np_x_ift, 'r')
   # plt.ylabel('x[n]')
   # plt.xlabel('n')

   plt.tight_layout()
   plt.show()
