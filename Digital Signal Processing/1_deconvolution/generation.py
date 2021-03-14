"""
Created on Thu Mar 11 11:30 2021

@author: ZYD

Digital Signal Processing: Homework 1
"""


import cv2 as cv
import numpy as np
from conv2mul import convolution_as_maultiplication


def draw(img):
    """画直线"""
    # cv.line(img, (210,170), (210,250), (250,250,250), 3, cv.LINE_8)
    # cv.line(img, (170,210), (250,210), (250,250,250), 3, cv.LINE_8)

    """画多条直线"""
    line1 = np.array([[210,170],  [210,250]], np.int32).reshape((-1, 1, 2))
    line2 = np.array([[170,210],  [250,210]], np.int32).reshape((-1, 1, 2))
    cv.polylines(img, [line1, line2], True, (250, 250, 250))
    
    """画椭圆"""
    cv.ellipse(img, (190, 45), (45, 65), 90, 0, 360, (50, 50, 50), -1)
    cv.ellipse(img, (190, 90), (30, 55), 90, 0, 360, (110, 110, 110), -1)

    """画多边形"""
    pts = np.array([[0, 90], [100, 90], [100, 190]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, (150, 150, 150))  
    cv.fillPoly(img, [pts], (190, 190, 190))
    cv.imwrite("img_ori.jpg", img)

    return img

def Gauss_kernel(ksize, sigma):
    kernel_1D = cv.getGaussianKernel(ksize, sigma)
    kernel_2D = kernel_1D * kernel_1D.T
    return kernel_2D


def Gauss_conv(img):
    kernel = Gauss_kernel(9, 4)
    img_conv = cv.filter2D(img, -1, kernel)
    return img_conv, kernel


def Gauss_noise(img, mean, variance):
    img = np.array(img/255, dtype=float)
    noise = np.random.normal(mean, variance, img.shape)
    img_noise = img + noise
    img_noise = np.clip(img_noise, 0, 1.0)
    img_noise = np.uint8(img_noise*255)

    # cv.imshow('img_noise', img_noise)
    cv.imwrite("img_noise.jpg", img_noise)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    return img_noise


def kernel2A(kernel, img, img_size):
    if img_size[0] == img_size[1]:
        n = img_size[0]
    else:
        print("Haven't implement the algortithm for rectangular images.")
    print(img[-1].shape)
    Ah, vector_img = convolution_as_maultiplication(img[:, :, 0], kernel)
    print(Ah.shape)
    print(vector_img.shape)

    # Ah = np.reshape(Ah, [])
    # print(Ah.shape)

    # Ah = []
    # for i in range(n):
    #     column = np.zeros([n + 2, n + 2], np.uint8)
    #     column[i:i + 9, ] = kernel
    #     Ah.append(column)
    return Ah, vector_img

if __name__ == "__main__":
    img_blank = 5*np.ones([256, 256, 3], np.uint8) #黑色图片
    img = draw(img_blank)
    img_conv, kernel = Gauss_conv(img)
    img_noise = Gauss_noise(img_conv, 0, 0.02)

    print("kernel:", kernel.shape)
    # Ah = kernel2A(kernel, img_noise, [256, 256])
