import numpy as np  
from scipy import interpolate  
import matplotlib.pyplot as plt
import matplotlib.cm as cm  
from Gauss import Gauss


def func(x, y, sigma):  
    return np.exp(-(x**2 + y**2) / (2 * sigma**2))
    # return (x+y)*np.exp(-5.0*(x**2 + y**2)) 

def my_1D_interpolate(x):
    fs = 0.9
    x_re = np.zeros(101)
    t = np.linspace(-5, 5, num=101)
    n = np.linspace(-5*fs, 5*fs, num=21)
    
    for i in range(len(x)):   
        i_ = np.ones(101) * n[i] / fs
        x_re += x[i] * np.sinc(fs*(t - i_))

    return x_re

def my_2D_interpolate(z, x0, y0):
    z_list = []
    for i in range(z.shape[0]):
        z_list.append(my_1D_interpolate(z[i, :]))
    z_re = np.array(z_list)

    z_list = []
    for i in range(z_re.shape[1]):
        z_list.append(my_1D_interpolate(z_re[:, i]))
    z_re = np.array(z_list)
    return z_re

def plot(x, y, x_sa, y_sa, z, z_sa, z_re):
    plt.figure(figsize=(20,20))
    ax1 = plt.subplot(1, 3, 1, projection = '3d')  
    surf1 = ax1.plot_surface(x, y, z, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0.5, antialiased=True)  
    ax1.set_xlabel('x')  
    ax1.set_ylabel('y')  
    ax1.set_zlabel('z')  
    ax1.set_title("Original Gauss signal")

    ax2 = plt.subplot(1, 3, 2, projection = '3d')  
    surf2 = ax2.plot_surface(x_sa, y_sa, z_sa, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0.5, antialiased=True)  
    ax2.set_xlabel('x_sa')  
    ax2.set_ylabel('y_sa')  
    ax2.set_zlabel('z_sa')  
    ax2.set_title("Sampled signal")
 
    ax3 = plt.subplot(1, 3, 3, projection = '3d')  
    surf3 = ax3.plot_surface(x, y, z_re, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0.5, antialiased=True)  
    ax3.set_xlabel('x_re')  
    ax3.set_ylabel('y_re')  
    ax3.set_zlabel('z_re')
    ax3.set_title("Interpolated signal")

    ax1.view_init(30,30)
    ax2.view_init(30,30)
    ax3.view_init(30,30)

    plt.tight_layout(pad=4) 
    plt.savefig('2D_Gauss_Sa_Re.png', dpi=600)
    plt.show() 

if __name__ == "__main__":
    sigma = 2
    x = np.linspace(-5, 5, 101)
    y = np.linspace(-5, 5, 101)
    x, y = np.meshgrid(x, y) 
    z = func(x, y, sigma)

    x_sa = np.linspace(-5, 5, 21)  
    y_sa = np.linspace(-5, 5, 21)  
    x_sa, y_sa = np.meshgrid(x_sa, y_sa)
    z_sa = func(x_sa, y_sa, sigma)

    # gt = interpolate.interp2d(x_sa, y_sa, z_sa, kind='cubic') # scipy插值函数 
    # z_gt = gt(x_re, y_re)

    z_re = my_2D_interpolate(z_sa, x_sa, y_sa) / 5
    print("error =", np.mean(np.abs(z_re - z)))

    plot(x, y, x_sa, y_sa, z, z_sa, z_re)