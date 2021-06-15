import os

os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2, 60).__str__()
import cv2

if __name__ == "__main__":
    # image = cv2.imread("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/domain00.tif")
    # with open("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/domain00.csv", "w") as csv_file:
    #     print(len(image))

    file = open("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/trex_fpga_log/ED_DIF.log", "r")
    lines = file.readlines()
    image_data = []
    for line in lines:
        image_data.append([format(int(data, 16), "032b") for data in line.split()])

    print(image_data[0][1])
    csv_data = []
    for chunks in image_data[1:]:
        csv_data.append(''.join(chunks))
    with open("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/trex_fpga_log/ED_TREX_DIF_REGISTER.csv", "w")as file:
        for chunk in csv_data:
            file.write(','.join(chunk) + "\n")

