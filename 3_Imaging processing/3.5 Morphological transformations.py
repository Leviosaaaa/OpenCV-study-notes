# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:37:21 2020

@author: ZYD

3.5 Morphological transformations

【学习内容】
使用cv.erode(), cv.dilate(), cv.morphologyEx()。
进行腐蚀、膨胀、开运算、闭运算等形态操作。

【代码内容】
形态转换
"""

import cv2 as cv
import numpy as np

img = cv.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
#腐蚀:孤立的白色区域被腐蚀为黑色
erosion = cv.erode(img, kernel, iterations = 1)
#膨胀：孤立的白色区域膨大
dilation = cv.dilate(img, kernel, iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
#闭运算：膨胀后再腐蚀，常用于去除对象上的黑色斑点
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
#形态学梯度：给出对象的轮廓
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
#顶帽：原图与开运算之差
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
#黑帽：原图与闭运算之差
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow('erosion', erosion)
#cv.imshow('dilation', dilation)
#cv.imshow('opening', opening)
#cv.imshow('closing', closing)
#cv.imshow('gradient', gradient)
#cv.imshow('tophat', tophat)
#cv.imshow('blackhat', blackhat)
cv.waitKey(0)
cv.destroyAllWindows()

