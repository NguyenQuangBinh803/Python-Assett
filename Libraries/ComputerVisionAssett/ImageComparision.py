import cv2
from skimage.measure import compare_ssim
import os
import time


def main():
    path = "TEST_DATA/20210116_IMG_DATA_2/"
    list_dir = os.listdir(path)
    for file in list_dir:
        for file_2 in list_dir:
            start_time = time.time()
            image_1 = cv2.imread(path + file, 0)
            image_2 = cv2.imread(path + file_2, 0)

            print(time.time() - start_time, compare_ssim(image_1, image_2))


if __name__ == "__main__":
    main()
