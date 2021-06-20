import cv2
import numpy as np

from imutils import contours


for i in range(1,8):
    img = cv2.imread('icon'+str(i)+'.png', 0)
    kernel = np.ones((4, 4), np.uint8)
    img = cv2.dilate(img, kernel, iterations=4)
    cv2.imwrite('icon'+str(i)+'.png', img)
