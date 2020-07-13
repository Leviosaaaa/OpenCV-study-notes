# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:06:42 2020

@author: ZYD

2.2 Arithmetic operations of images

【学习内容】
使用cv.add(), cv.addWeighted()。
图像的加法、减法、按位运算。

【代码内容】
图片的叠加
"""


import numpy as np
import cv2 as cv


# In[1]:加法
x = np.uint8([250])
y = np.uint8([10])
print(cv.add(x, y))  #openCV加法是饱和运算：250 + 10 = 260 -> 255
print(x + y)  #numpy加法是模运算：(250 + 10) % 256 = 4


# In[2]:图像融合
img1 = cv.imread('test1.jpg')
img2 = cv.imread('test2.jpg')
new_img = cv.addWeighted(img1, 0.3, img2, 0.7, 0)  #0.3和0.7是img1和img2的权重
cv.imshow('new_img', new_img)
cv.waitKey(0)
cv.destroyAllWindows()


# In[3]:按位运算
img1 = cv.imread('test1.jpg')
img2 = cv.imread('test2.jpg')
#
rows, cols, channels = img2.shape
ROI = img1[0:rows, 0:cols]
#
img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshod(img2_gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
#
img1_bg = cv.bitwise_and(ROI, ROI, mask = mask_inv)
#
img1_fg = cv.bitwise_and(img2, img2, mask = mask)
#
img_new = cv.add(img_bg, img2_fg)
img1[0:row, 0:cols] = img_new

cv.imshow('res', img1)
cv.waitKey()
cv.destroyAllWindows()


 