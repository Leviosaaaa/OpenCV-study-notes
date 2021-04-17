import cmath
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# from FFT import fft

def fft(x):
    return np.fft.fft(x)

def ifft(F):
    return np.fft.ifft(F)

def FFT2D(img):
    return fft(fft(img).T).T

def iFFT2D(F):
    return ifft(ifft(F).T).T

def FFT_SHIFT(img):
    M, N = img.shape
    M = int(M/2)
    N = int(N/2)
    return np.vstack((np.hstack((img[M:,N:],img[M:,:N])),np.hstack((img[:M,N:],img[:M,:N]))))


if __name__ == "__main__":
    img = cv.imread('Van.jpg')
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    F = np.fft.fft2(img / 255.)
    img_ifft = iFFT2D(F)
    img_ifft = np.array(255*img_ifft, dtype=np.uint8)
    cv.imwrite('van_ifft.jpg', img_ifft)
    F = abs(FFT_SHIFT(FFT2D(img)))

    x = np.arange(F.shape[1])
    y = np.arange(F.shape[0])
    X, Y = np.meshgrid(x, y)

    ax = plt.axes(projection='3d')
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.set_zlabel("log[1+F(jw)]", fontsize=12)
    ax.set_title('2D Fourier Transform')
    ax.plot_surface(X, Y, np.log(1+F), rstride=1, cstride=1, cmap='viridis', alpha = 0.3, edgecolor='none')
    
    plt.show()
