# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:33:50 2020

@author: ZYD

4.5 SUFT (Speeded-Up Robust Features)

【学习内容】
SUFT是SIFT的加速版本。
使用SURF.detect()，surf.compute()。


【代码内容】

"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lfy.jpg', 0)
surf = cv.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img, None)

# 检查海森矩阵阈值
print(surf.getHessianThreshold())
# 我们将其设置为?(建议值50000）。这仅用于表示图片。在实际情况下，最好将值设为300-500
surf.setHessianThreshold(12000)
# 再次计算关键点并检查其数量。
kp, des = surf.detectAndCompute(img, None)
print(len(kp))

img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()


# 找到算符的描述
print( surf.descriptorSize() )
# 表示flag “extened” 为False。
surf.getExtended()
# 因此，将其设为True即可获取128个尺寸的描述符。
surf.setExtended(True)
kp, des = surf.detectAndCompute(img,None)
print( surf.descriptorSize() )
print( des.shape )
