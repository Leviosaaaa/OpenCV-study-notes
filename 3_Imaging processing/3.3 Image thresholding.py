# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:59:56 2020

@author: ZYD

3.3 Image thresholding

【学习内容】
使用cv.threshold(), cv.adaptiveTreshold()。
了解简单阈值，自适应阈值和Otsu阈值。

【代码内容】
色彩空间转换
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('test2.jpg', 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
    plt.subplot(2, 3, i + 1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt,yticks([])
plt.show()