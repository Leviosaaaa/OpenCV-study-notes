# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:39:59 2020

@author: ZYD

1.2 Video basic
1.2.1 Video captured by camera
"""

"""
【学习内容】
学习使用cv.VideoCapture()
函数参数可以是摄像头编号，也可以是是视频文件名。
函数返回值是一个VideoCapture对象。对于此对象，可以逐帧捕获图片。
【代码内容】
从电脑相机中捕获视频，并显示黑白的视频
"""

import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)  #后置摄像头
#cap = cv.VideoCapture(1)  #前置摄像头

if not cap.isOpened():  #.isOpen()函数返回bool值，表示摄像头是否初始化
    print("Cannot open camera")
    exit()
    
while True:
    ret, frame = cap.read()  #.read()函数返回bool值，表示是否正常读取帧
    if not ret:  #ret为False时意味着未能正常读取帧
        print("Can't receive frame (stream end?). Exiting...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  #将读取的帧frame变成灰度图像，并保存在gray中
    cv.imshow('frame', gray)  #显示灰度图像
    if cv.waitKey(1) == ord('q'):  #键盘按下q键时退出
        break
    
cap.release()  #释放捕获器
cv.destroyAllWindows()
