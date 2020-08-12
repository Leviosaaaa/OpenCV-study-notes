# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:31:41 2020

@author: ZYD

3.13 Hough line transform

【学习内容】
使用cv.HoughLines()。


【代码内容】
识别图片中的直线
"""

import cv2 as cv
import numpy as np

img = cv.imread('building.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize = 3)
lines = cv.HoughLines(edges, 1, np.pi/180, 200)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 - 1000*b)
    y1 = int(y0 + 1000*a)
    x2 = int(x0 + 1000*b)
    y2 = int(y0 - 1000*a)
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imwrite('Hough lines.jpg', img)
