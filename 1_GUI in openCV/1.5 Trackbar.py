# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:18:29 2020

@author: ZYD

1.5 Trackbar
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
cv.namedWindow('image')  #创建窗口

#创建颜色变化的滑动条
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

#创建开关滑动条
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv.getTrackbarPos('R', 'image')  #获得滑动条的当前位置
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()

    