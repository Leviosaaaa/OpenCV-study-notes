# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:47:46 2020

@author: ZYD

3.2 Geometric transformations of images

【学习内容】
使用cv.getPerspectiveTransforn()。
对图像进行平移、旋转、仿射变换等几何变换。

【代码内容】
图像几何变换
"""

import cv2 as cv
import numpy as np

#缩放
img = cv.imread('test1.jpg')
res = cv.resize(img, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)
height, width = img.shape[:2]
res = cv.resize(img, (2*width, 2*height), interpolation = cv.INTER_CUBIC)
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()