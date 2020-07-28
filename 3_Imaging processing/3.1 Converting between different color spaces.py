# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:50:25 2020

@author: ZYD

3 Image processing
3.1 Converting between different color spaces

【学习内容】
使用cv.cvtColor(), cv.inRange()。
将图像从一个色彩空间转换到另一个。
提取视频中的彩色对象。

【代码内容】
色彩空间转换
"""

import cv2 as cv
import numpy as np

#flags = [i for i in dir(cv) if i.startswith('COLOR_')]
#print(flags)

cap = cv.VideoCapture(0)
while(1):
    #读取帧
    _, frame = cap.read()
    #转换颜色空间，BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #定义HSV中的颜色范围
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    #设置HSV阈值，只取蓝色
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    #将mask与图像逐像素相加
    res = cv.bitwise_and(frame, frame, mask = mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
