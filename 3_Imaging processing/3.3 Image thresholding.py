# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:59:56 2020

@author: ZYD

3.3 Image thresholding

【学习内容】
使用cv.threshold(), cv.adaptiveTreshold()。
了解简单阈值，自适应阈值和Otsu阈值。

【代码内容】
图像阈值
P.S.跟官方教程的效果图不太一样，原因还没有搞清楚
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# In[1]: 简单阈值
#阈值是全局的
img = cv.imread('gray_gradient.jpg', 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# In[2]: 自适应阈值
#根据图片不同区域的光线条件，给出各个局部的阈值
img = cv.imread('gray_test.jpg', 0)
#全局阈值为127
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#Otsu阈值
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
#Gauss滤波后再采用Otsu阈值
blur = cv.GaussianBlur(img, (5,5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
#绘制所有图像及其直方图
images = [img, 0,th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v = 127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gauss Filtered Image', 'Histogram', "Otsu's Thresholding"]
for i  in range(3):
    plt.subplot(3, 3, i*3 + 1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3 + 2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3 + 1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3 + 3),plt.imshow(images[i*3 + 2],'gray')
    plt.title(titles[i*3 + 2]), plt.xticks([]), plt.yticks([])
plt.show()

# In[3]:Otsu二值化的实现
img = cv.imread('gray_test.jpg', 0)
blur = cv.GaussianBlur(img,(5,5),0)
# 寻找归一化直方图和对应的累积分布函数
hist = cv.calcHist([blur],[0],None,[256],[0,256])
hist_norm = hist.ravel()/hist.max()
Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1
for i in range(1,256):
    p1,p2 = np.hsplit(hist_norm,[i]) # 概率
    q1,q2 = Q[i],Q[255]-Q[i] # 对类求和
    b1,b2 = np.hsplit(bins,[i]) # 权重
    # 寻找均值和方差
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
    # 计算最小化函数
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i
# 使用OpenCV函数找到otsu的阈值
ret, otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print( "{} {}".format(thresh,ret) )