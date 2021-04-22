import cv2

if __name__ == "__main__":

    img = cv2.imread("C:/Users/ASUS/Documents/test_folder_1/test_segmentation/2.jpg")
    cv2.imwrite("imgorg.png",img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png",gray)

    ret, thresh = cv2.threshold(gray, 199, 255, cv2.THRESH_BINARY_INV)

    edge = cv2.Canny(gray, 90,100)
    # cv2.dilate(edge, cv2.getStructuringElement((3,3)))

    cv2.imwrite("thresh.png",edge)
