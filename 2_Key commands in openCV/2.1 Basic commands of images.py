# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:02:42 2020

@author: ZYD

2.1 Basic commands of images
"""

"""
【学习内容】
学习访问、修改像素值，访问图像属性，设置ROI，分割、合并图像。
【代码内容】
基本操作示例
"""


import numpy as np
import cv2 as cv


img = cv.imread('test.jpg')


# In[1]:访问、修改像素值
#通过行列坐标访问像素值
px = img[100, 100]
print(px)

#仅访问蓝色像素
blue = img[100, 100, 0]
print(blue)

#修改像素值
img[100, 100] = [255, 255, 255]
print(img[100,100])

#访问红色
img.item(10, 10, 2)
img.itemset((10,10,2), 100)
print(img.item(10, 10, 2))


# In[2]:访问图像属性
#图片尺寸：返回行数、列数、通道数（灰度图像没有这一项）
print(img.shape)

#像素总数
print(img.size)

#图像数据类型
print(img.dtype)


# In[3]:图像感兴趣区域ROI
ROI = img[280:340, 330:390]  #选中，赋值
img[273:333, 100:160] = ROI  #粘贴到另一个位置


# In[4]:拆分、合并图像通道
b, g, r = cv.split(img)
b = img[:, :, 2] = 0
img[:, :, 2] = 0
img = cv.merge((b, g, r))


