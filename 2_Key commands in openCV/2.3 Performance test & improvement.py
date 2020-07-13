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


c1 = cv.getTickCount()
c2 = cv.getTickCount()
time = (c1 - c2) / cv.getTickFrequency 


