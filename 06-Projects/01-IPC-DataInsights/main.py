



if __name__ == '__main__':
    file = open("C:/Users/ASUS/Documents/test_folder_1/test_ipc_log_data/IMGLIB_LOG_ED.log", "r", encoding="utf-8")
    process_count = 0
    process_previous = ""

    for line in file.readlines():
        if "complete[" in line :

            if process_previous == "":
                process_previous = line.split()[3]
                process_count = 0
            elif process_previous == line.split()[3]:
                process_count += 1
            elif process_previous != line.split()[3]:
                process_count = 0
                process_previous = line.split()[3]
            print(line.split()[3], process_count)
