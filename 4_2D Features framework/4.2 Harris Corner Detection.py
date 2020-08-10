# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:49:24 2020

@author: ZYD

4 2D Features framework
4.2 Harris corner detection

【学习内容】
学习Harris角检测。
使用cv.cornerHarris(),cv.cornerSubPix()。

【代码内容】
检测角点。
"""

# In[1]
import numpy as np
import cv2 as cv
filename = 'test1.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
#result用于标记角点，并不重要
dst = cv.dilate(dst,None)
#最佳值的阈值，它可能因图像而异。
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
    
# In[2]
import numpy as np
import cv2 as cv
filename = 'DSC_0932.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 寻找哈里斯角
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)
ret, dst = cv.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
# 寻找质心
ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)
# 定义停止和完善拐角的条件
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
# 绘制
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]
cv.imwrite('subpixel5.jpg',img)
cv.imshow('subpixel5.jpg',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()