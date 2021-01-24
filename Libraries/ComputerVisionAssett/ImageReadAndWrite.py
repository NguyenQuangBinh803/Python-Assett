import cv2

if __name__ == "__main__":
    image = cv2.imread("IMG_20170910_103406.jpg")
    
    print(image.shape)
    cv2.imshow("image", image)
    cv2.waitKey(0)