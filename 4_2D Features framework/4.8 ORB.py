# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:34:24 2020

@author: ZYD

4.8 ORB (Oriented FAST and Rotated BRIEF)

【学习内容】
使用orb.detect(), orb.compute()。

【代码内容】
使用ORB检测关键点，计算描述符。
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('test1.jpg', 0)
# 初始化ORB检测器
orb = cv.ORB_create()
# 用ORB寻找keypoint
kp = orb.detect(img, None)
# 用ORB计算描述符
kp, des = orb.compute(img, kp)
# 仅绘制关键点的位置，而不绘制大小和方向
img2 = cv.drawKeypoints(img, kp, None, color = (0,255,0), flags = 0)
plt.imshow(img2), plt.show()