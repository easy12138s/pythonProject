# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2382019442@qq.com
    @software: PyCharm
    @file: 灰度降噪处理.py
    @time: 2023/10/24 13:31
"""
import cv2 as cv
import numpy as np

img1 = cv.imread('./images/topcheer.png', 0)
ret, binary = cv.threshold(img1, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

cv.imshow('one', binary)

cv.waitKey(0)
cv.imwrite('a.txt', img1)