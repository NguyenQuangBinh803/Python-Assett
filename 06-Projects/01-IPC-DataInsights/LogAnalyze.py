from LogData import LogData


class LogAnalyze:
    def __init__(self, file_name):
        self.log_package = []
        self.log_package_count = 0

        file = open(file_name, "r", encoding="utf-8")
        process_count = 0
        process_previous = ""
        self.log_package.append(LogData())
        for line in file.readlines():
            self.log_package[self.log_package_count].log_package_data += line
            if "complete[" in line:
                if process_previous == "":
                    process_previous = line.split()[3]
                    self.log_package[self.log_package_count].log_package_name = process_previous
                    process_count = 0
                elif process_previous == line.split()[3]:
                    process_count += 1
                elif process_previous != line.split()[3]:
                    process_count = 0
                    self.log_package.append(LogData())
                    self.log_package_count += 1
                    process_previous = line.split()[3]
                    self.log_package[self.log_package_count].log_package_name = process_previous
                # print(line.split()[3], process_count)
        # print(len(self.log_package))

if __name__ == "__main__":
    log_analyze = LogAnalyze("C:/Users/ASUS/Documents/test_folder_1/test_ipc_log_data/IMGLIB_LOG_ED.log")
    print(log_analyze.log_package[3].log_package_data)
