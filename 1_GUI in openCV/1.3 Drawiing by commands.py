# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:00:59 2020

@author: ZYD

1.3 openCV的绘图功能
"""

"""
【学习内容】
学习使用cv.line(),cv.circle(),cv.rectangle(),cv.ellipse(),cv.putText()。
函数参数有颜色，线的粗细，线的类型。
【代码内容】
绘制指定图形
"""


import cv2 as cv
import numpy as np


#创建黑色背景
img = np.zeros((512,512,3), np.uint8)

#画直线： (0,0)是起点, (511,511)是终点, (255,0,0)是蓝色, 5是线的粗细
cv.line(img, (0,0), (511,511), (255,0,0), 5) 

#画矩形
cv.rectangle(img, (384,0), (510,128), (0,255,0), 3)

#画圆圈
cv.circle(img, (447,63), 63, (0,0,255), -1)

#画椭圆：(256,256)是中心, (100,50)分别是长短轴长, 0是椭圆沿逆时针旋转的角度, 0和180是椭圆弧开始和结束角度
cv.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

#画多边形
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0,255,255))  #True代表绘制闭合多边形，若False则相当于绘制一组线条

#在图片上写字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'openCV', (10,500), font, 4, (255,255,255), 2, cv.LINE_AA)


cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()