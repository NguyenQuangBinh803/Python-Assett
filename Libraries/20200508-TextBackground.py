import numpy as np
import cv2 
from matplotlib import pyplot as plt
img = cv2.imread('1.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

sensitivity = 165
lower_white = np.array([0,0,255-sensitivity])
upper_white = np.array([255,sensitivity,255])
##dilation = cv2.dilate(img,kernel,iterations = 1)

    # Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
cv2.imshow('mask',mask)
res = cv2.bitwise_and(img,img, mask= mask)
cnts = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
he,wi,_= img.shape
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    if y==0 or y+h == he:
        mask[y:y+h,x:x+w] = 0
##cv2.imshow('frame',img)
cv2.imshow('mask1',mask)
##cv2.imshow('res',res)

coords = np.column_stack(np.where(mask > 0))
angle = cv2.minAreaRect(coords)[-1]
# the `cv2.minAreaRect` function returns values in the
# range [-90, 0); as the rectangle rotates clockwise the
# returned angle trends to 0 -- in this special case we
# need to add 90 degrees to the angle
if angle < -45:
	angle = -(90 + angle)
# otherwise, just take the inverse of the angle to make
# it positive
else:
	angle = -angle

(h, w) = mask.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(mask, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

cv2.imshow("Rotated", rotated)


