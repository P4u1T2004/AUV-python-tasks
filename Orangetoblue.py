import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('/Users/paul/Desktop/opencv/Opencvsamples/sample1.jpeg')

    
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower_blue = np.array([80, 50, 50])
upper_blue = np.array([130, 255, 255])
lower_red = np.array([160, 80, 20])
upper_red = np.array([179, 255, 255])
mask1 = cv.inRange(hsv, lower_blue, upper_blue)
mask2 = cv.inRange(hsv, lower_red,upper_red)
mask = cv.bitwise_or(mask1,mask2)

res = cv.bitwise_and(img,img, mask= mask)
cv.imshow('img',img)
cv.imshow('mask',mask)
cv.imshow('res',res)
k = cv.waitKey(0)
