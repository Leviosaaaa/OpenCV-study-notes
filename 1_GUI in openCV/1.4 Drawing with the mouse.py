# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:28:05 2020

@author: ZYD
"""

"""
【学习内容】
学习使用cv.setMouseCallback()。
了解如何在openCV中处理鼠标事件。
【代码内容】
使用鼠标绘制圆圈或矩形。
"""


import cv2 as cv
import numpy as np


# In[1]
events = [i for i in dir(cv) if 'event' in i]
print(events)


# In[2]
ix, iy = -1, -1
drawing = False
mode = True

#鼠标的回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing == True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
            else:
                cv.circle(img, (x,y), 5, (0,255,0), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
        else:
            cv.circle(img, (x,y), 5, (0,0,255), -1)
                
            
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)  #指定draw_circle是鼠标的回调函数

while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()


