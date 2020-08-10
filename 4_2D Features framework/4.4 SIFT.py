# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:33:07 2020

@author: ZYD

4.4 SIFT

【学习内容】
学习SIFT算法。
使用cv.xfeatures2d.SIFT_create()，sift.detect()。


【代码内容】
调用SIFT的API，找出并标记关键点。
"""

import numpy as np
import cv2 as cv
 
img = cv.imread('DSC_0874.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
#img = cv.drawKeypoints(gray, kp, img)
img = cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite('sift_keypoints.jpg', img)


"""
sift = cv.xfeatures2d.SIFT_create() 
kp, des = sift.detectAndCompute(gray,None)
#kp是一个关键点列表，des是一个数字数组。
"""