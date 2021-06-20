import cv2

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized
import numpy as np
img = cv2.imread('1.png')
blur = cv2.blur(img,(3,3))
blur2 = cv2.GaussianBlur(img,(3,3),0)

##absd=cv2.equalizeHist(cv2.cvtColor(cv2.absdiff(blur2,blur),cv2.COLOR_BGR2GRAY))
##kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
##img = cv2.filter2D(img, -1, kernel)
##cv2.imshow('im', img)
##blur = cv2.GaussianBlur(img,(3,3),0)
##smooth = cv2.addWeighted(blur,1.5,img,-0.5,0)
edges = cv2.Canny(blur,0,255)
cv2.imwrite('smooth.png', edges)
