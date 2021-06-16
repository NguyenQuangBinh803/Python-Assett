import tifffile
import glob
import os

if __name__ == "__main__":
    file_num = 1
    sample = 16384
    files = glob.glob("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/*.tif")
    for file in files:
        print(file, os.path.basename(file)[:-4])
        tif = tifffile.imread(file)
        print(tif.dtype, tif.shape, tif[0][0], str(int(tif[0][0])), round(tif.shape[0] / sample))
        count = 0
        for n in range(0, round(tif.shape[0] / sample)):
            tifffile.imwrite("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/" + os.path.basename(file)[:-4] + str(file_num) + "_clone_%s.png" % str(n),
                             tif[sample * n:sample * (n + 1)])
            count = n
        tifffile.imwrite("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/" + os.path.basename(file)[:-4] + str(file_num) + "_clone_%s.png" % str(count + 1),
                         tif[sample * count:tif.shape[0]])
