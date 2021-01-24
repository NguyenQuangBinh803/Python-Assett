import cv2
import numpy as np
from matplotlib import pyplot as plt


if __name__ == "__main__":
    img = cv2.imread('E:/2020 - Images/I',1)
    rows,cols = img.shape[:2]
    zeros = np.copy(img)
    zeros[:,:,:] = 0
    a = cv2.getGaussianKernel(cols,900)
    b = cv2.getGaussianKernel(rows,900)
    c = b*a.T
    d = c/c.max()
    output_image = img*d

    cv2.imshow('vig2.png',output_image)
    cv2.waitKey(0)