# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:49:51 2020

@author: ZYD

3.6 Image gradients

【学习内容】
使用cv.Sobel(), cv.Scharr(), cv.Laplacian()。
对图像进行高通（梯度）滤波。

【代码内容】

"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('logo.png', 0)
laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0,ksize = 5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1,ksize = 5)
plt.subplot(2, 2, 1), plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()