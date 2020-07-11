# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:22:39 2020

@author: HB-CMCC

1.2Video basic
1.2.3 保存视频
"""

"""
【学习内容】
学习使用cv.VideoCapture()
函数参数可以是摄像头编号，也可以是是视频文件名。
函数返回值是一个VideoCapture对象。对于此对象，可以逐帧捕获图片。
【代码内容】
从电脑相机中捕获视频，并保存翻转

的视频
"""

import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break
    frame = cv.flip(frame, 0)
    out.write(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
