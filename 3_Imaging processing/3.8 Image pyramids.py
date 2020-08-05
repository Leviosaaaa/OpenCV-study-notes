# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:35:11 2020

@author: ZYD

3.8 Image pyramids

【学习内容】
使用cv.pyrUp(), cv.pyrDown()。
学习图像金字塔。


【代码内容】

"""


import numpy as np, sys
import cv2 as cv
import math

A = cv.imread('_2.jpg')
B = cv.imread('_1.jpg')

# 生成A的高斯金字塔
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)
    
# 生成B的高斯金字塔
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# 生成A的拉普拉斯金字塔
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1], GE)
    lpA.append(L)

# 生成B的拉普拉斯金字塔
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1], GE)
    lpB.append(L)

# 现在在每个级别中添加左右两半图像 
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    cols = math.floor(cols/2)
    ls = np.hstack((la[:,0:cols], lb[:,cols:]))
    LS.append(ls)

# 现在重建
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])

# 图像与直接连接的每一半
cols = math.floor(cols/2)
real = np.hstack((A[:,:cols], B[:,cols:]))
cv.imwrite('Pyramid_blending2.jpg', ls_)
cv.imwrite('Direct_blending.jpg', real)


"""
由于程序采用6层金字塔，一次其图片像素的行数和列数要能够被（2X2X2X2X2X2）整除
否则计算过程中像素矩阵对不上会报错subtract对不上号。
"""