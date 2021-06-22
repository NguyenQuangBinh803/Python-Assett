
def ExtractProcessingPieces():
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
        dmd_image = np.zeros((dmd_mirror_width, 4096), dtype=bool)

        for tif_row in range(0, tif.shape[0]):
            for n in range(0, int(tif.shape[1] / 4096)):
                print(len(tif[tif_row]), len(dmd_image[dmd_row]))
                file_text.write(','.join([str(int(data)) for data in tif[tif_row][n * 4096:(n + 1) * 4096]]) + "\n")
                # print(','.join([str(int(data)) for data in tif[tif_row][n * 4096:(n + 1) * 4096]]))
                dmd_image[dmd_row] = tif[tif_row][n * 4096:(n + 1) * 4096]
                # file_text.write(','.join([str(int(data)) for data in dmd_image[dmd_row]]) + "\n")
                # print(','.join([str(int(data)) for data in dmd_image[dmd_row]]))
                dmd_row += 1
                if dmd_row > dmd_mirror_width - 1:
                    dmd_row = 0
                    tifffile.imwrite("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/domain_image/dmd_image/dmd_image_" + str(dmd_count) + ".png", dmd_image)
                    dmd_count += 1
                    dmd_image = np.zeros((dmd_mirror_width, 4096), dtype=bool)

