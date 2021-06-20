import pytesseract
from pytesseract import Output
import cv2
img = cv2.imread('1.png')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
##    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi', roi)
    config = ("-l eng --oem 3 --psm 3")
    text = pytesseract.image_to_string(img, config=config)
    print(text)
cv2.imshow('img', img)
cv2.waitKey(0)
