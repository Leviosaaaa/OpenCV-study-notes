# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:04:10 2020

@author: ZYD

3.4 Smoothing images

【学习内容】
使用cv.filter2D()
使用低通滤波器模糊图像。
注：低通滤波有助于消除高频噪声，是图像模糊；高通滤波有助于在图像中找到边缘。

【代码内容】
图像模糊
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# In[1]: 2D卷积滤波
img = cv.imread('logo.png')
kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]). plt.yticks([])
plt.show()


# In[2]: 平均滤波，中心像素变为一个指定kernel大小的周围像素的平均值
img = cv.imread('logo.png')
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


# In[3]: Gauss模糊，使用Guass核
img = cv.imread('logo.png')
blur = cv.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


# In[4]: 中位模糊，中心像素变为一个指定kernel大小的周围像素的中位数
img = cv.imread('logo.png')
median = cv.medianBlur(img,5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()


# In[5]: 双边滤波，在去除噪声的同时保持边缘尖锐
img = cv.imread('logo.png')
blur = cv.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

