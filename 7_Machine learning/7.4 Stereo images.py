# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:33:05 2020

@author: ZYD
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
imgL = cv.imread('test1.jpg',0)
imgR = cv.imread('test2.jpg',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()