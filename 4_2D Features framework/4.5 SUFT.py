# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:33:50 2020

@author: ZYD

4.5 SUFT

【学习内容】
SUFT是SIFT的加速版本。
使用cv.xfeatures2d.SURF_create()，surf.detectAndCompute()。


【代码内容】

"""

img = cv.imread('lfy.jpg', 0)
surf = cv.xfeature2d.SURF_create(400)
kp, des = surf.detectAndCompute(img, None)
