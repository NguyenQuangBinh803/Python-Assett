import tifffile
import glob
import os
import numpy as np


def ExtractMultipleImages():
    file_num = 1
    sample = 16384
    files = glob.glob("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/01/*.tif")
    for file in files:
        print(file, os.path.basename(file)[:-4])
        tif = tifffile.imread(file)
        print(tif.dtype, tif.shape, tif[0][0], str(int(tif[0][0])), round(tif.shape[0] / sample))
        count = 0
        for n in range(0, round(tif.shape[0] / sample)):
            tifffile.imwrite("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/splitted_image/" + os.path.basename(file)[:-4] + str(file_num) + "_clone_%s.png" % str(n),
                             tif[sample * n:sample * (n + 1)])
            count = n
        tifffile.imwrite("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/splitted_image/" + os.path.basename(file)[:-4] + str(file_num) + "_clone_%s.png" % str(count + 1),
                         tif[sample * count:tif.shape[0]])


def ExtractProcessingPieces():
    file_num = 1
    sample = 4096
    files = glob.glob("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/01/*.tif")
    for file in files:
        print(file, os.path.basename(file)[:-4])
        tif = tifffile.imread(file)
        print(tif.dtype, tif.shape, tif[0][0], str(int(tif[0][0])), round(tif.shape[0] / sample), len(tif[0]))
        count = 0
        for n in range(0, round(tif.shape[0] / sample)):
            for m in range(0, int(tif.shape[1] / sample)):
                print(sample * m, sample * (m + 1))
                tifffile.imwrite(
                    "C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/processing_piece/" + os.path.basename(file)[:-4] + "_clone_%s_%s.png" % (str(n), str(m)),
                    tif[sample * n:sample * (n + 1), sample * m: sample * (m + 1)])

            count = n
        for m in range(0, int(tif.shape[1] / sample)):
            tifffile.imwrite(
                "C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/processing_piece/" + os.path.basename(file)[:-4] + "_clone_%s_%s.png" % (str(n), str(m)),
                tif[sample * count:tif.shape[0], sample * m:  (m + 1) * sample])


def ExtractToDMDData():
    file_num = 1
    sample = 16384
    files = glob.glob("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/01/*.tif")
    for file in files:
        print(file, os.path.basename(file)[:-4])
        tif = tifffile.imread(file)
        print(type(tif), tif.dtype, tif.shape, tif[0][0], str(int(tif[0][0])), round(tif.shape[0] / sample))
        dmd_count = 0
        dmd_row = 0
        dmd_mirror_width = 256
        dmd_image = np.zeros((dmd_mirror_width, 1024), dtype=bool)
        file_text = open("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/00.csv", "w")

        for tif_row in range(0, tif.shape[0]):
            for n in range(0, int(tif.shape[1] / 1024)):
                print(len(tif[tif_row]), len(dmd_image[dmd_row]))
                file_text.write(','.join([str(int(data)) for data in tif[tif_row][n * 1024:(n + 1) * 1024]]) + "\n")
                # print(','.join([str(int(data)) for data in tif[tif_row][n * 1024:(n + 1) * 1024]]))
                dmd_image[dmd_row] = tif[tif_row][n * 1024:(n + 1) * 1024]
                # file_text.write(','.join([str(int(data)) for data in dmd_image[dmd_row]]) + "\n")
                # print(','.join([str(int(data)) for data in dmd_image[dmd_row]]))
                dmd_row += 1
                if dmd_row > dmd_mirror_width - 1:
                    dmd_row = 0
                    tifffile.imwrite("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/dmd_image/dmd_image_" + str(dmd_count) + ".png", dmd_image)
                    dmd_count += 1
                    dmd_image = np.zeros((dmd_mirror_width, 1024), dtype=bool)


if __name__ == "__main__":
    ExtractProcessingPieces()
