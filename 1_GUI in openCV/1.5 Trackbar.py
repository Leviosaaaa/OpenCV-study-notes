# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:18:29 2020

@author: ZYD
"""

"""
【学习内容】
学习使用cv.getTrackbarPos(), cv.createTrackbar。
了解将滑动条固定到openCV窗口。
【代码内容】
在GUI中使用滑动条自定义的RGB颜色。
"""


import cv2 as cv
import numpy as np


def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8)  #创建黑色图像
cv.nameWindow('image')  #创建窗口

#创建颜色变化的滑动条
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)