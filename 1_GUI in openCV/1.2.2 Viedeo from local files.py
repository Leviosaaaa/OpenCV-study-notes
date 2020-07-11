# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:15:00 2020

@author: ZYD

1.2 Video basic
1.2.2 Video from local files
"""

"""
【学习内容】
学习使用cv.VideoCapture()
函数参数可以是摄像头编号，也可以是是视频文件名。
函数返回值是一个VideoCapture对象。对于此对象，可以逐帧捕获图片。
【代码内容】
从视频文件读取视频，并播放黑白视频
"""

import numpy as np
import cv2 as cv

cap = cv.VideoCapture("e.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Eixting...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(3) == ord('q'):  #使用cv.waitKey()控制时间，间接地控制播放速度
        break
    
cap.release()
cv.destroyAllWindows()

