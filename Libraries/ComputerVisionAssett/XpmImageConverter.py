import numpy as np
import cv2
import shutil

if __name__ == "__main__":
    with open("image_data.txt", "r") as file:
        lines = file.readline()
    row_count = 0
    col_count = 0
    image = np.zeros((140, 140, 1))
    for index, character in enumerate(lines):
        pixel_value = int(character, 16) * 255 / 16
        try:
            image[row_count][col_count] = pixel_value
        except IndexError:
            break
        col_count += 1
        if index % 140 == 0:
            col_count = 0
            row_count += 1
    print(image)
    cv2.imshow("image", image)
    cv2.waitKey(0)

