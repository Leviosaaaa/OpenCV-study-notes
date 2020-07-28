# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:39:13 2020

@author: ZYD

2.3 Performance test & improvement

【学习内容】
使用cv.getTickCount(), cv.addTickFrequency()。
衡量代码的性能，提高代码性能技巧。

【代码内容】
代码的运行计时和优化。
"""

import numpy as np
import cv2 as cv

img1 = cv.imread('test2.jpg')
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )

"""
c1 = cv.getTickCount()
c2 = cv.getTickCount()
time = (c1 - c2) / cv.getTickFrequency 
"""

