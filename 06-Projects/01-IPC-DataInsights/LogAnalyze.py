#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2021"
__status__ = "At this rate we just need to interface the client level of the factory "
__version__ = "2021.06.14"

import re
from LogPackageFactory import LogPackageFactory


class LogAnalyze:
    def __init__(self):
        self.log_package = []
        self.log_package_count = 0
        self.log_package_factory = LogPackageFactory()

    def AnalyzeLogPackageGenerate(self, file_name):
        file = open(file_name, "r",encoding="EUC-JP")
        # file = open(file_name, "r", encoding="utf-8")
        process_count = 0
        process_previous = ""
        temporary_package_data = ""

        for line in file.readlines():
            temporary_package_data += line

            if "complete[" in line:
                if process_previous == "":
                    process_previous = line.split()[3]
                    print(process_previous)
                    self.log_package.append(self.log_package_factory.FactoryProduce(process_previous))
                    self.log_package[self.log_package_count].log_package_data = temporary_package_data
                    temporary_package_data = ""

                else:
                    process_previous = line.split()[3]
                    self.log_package_count += 1
                    self.log_package.append(self.log_package_factory.FactoryProduce(process_previous))
                    self.log_package[self.log_package_count].log_package_data = temporary_package_data
                    temporary_package_data = ""


    # def AnalyzeLogPackageGenerate_1(self, file_name):
    #     # file = open(file_name, "r", encoding="utf-8")
    #     file = open(file_name, "r")
    #     process_count = 0
    #     process_previous = ""
    #     self.log_package.append(LogPackage())
    #     for line in file.readlines():
    #         self.log_package[self.log_package_count].log_package_data += line
    #         if "complete[" in line:
    #             if process_previous == "":
    #                 process_previous = line.split()[3]
    #                 self.log_package[self.log_package_count].log_package_name = process_previous
    #                 process_count = 0
    #             elif process_previous == line.split()[3]:
    #                 process_count += 1
    #             elif process_previous != line.split()[3]:
    #                 process_count = 0
    #                 self.log_package.append(LogPackage())
    #                 self.log_package_count += 1
    #                 process_previous = line.split()[3]
    #                 self.log_package[self.log_package_count].log_package_name = process_previous
    #             # print(line.split()[3], process_count)
    #     # print(len(self.log_package))

import glob

if __name__ == "__main__":

    log_analyze = LogAnalyze()
    # log_files = glob.glob("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/*.log")
    # for log_file in log_files:
    #     print(log_file)
    #     log_analyze.AnalyzeLogPackageGenerate(log_file)

    log_analyze.AnalyzeLogPackageGenerate("C:/Users/binh_nguyen/Documents/test_folder_1/test_ipc_log_data/IMGLIB1_20210604.log")

    # Filter the startTrace package
    imgLib_startTrace_log_package = [package for package in log_analyze.log_package if package.log_package_name == "imgLib_startTrace"]

    # Filter the expStandby package
    imgLib_expStandby_log_package = [package for package in log_analyze.log_package if package.log_package_name == "imgLib_expStandby"]
    print(len(imgLib_expStandby_log_package))
    for log_pkg in imgLib_expStandby_log_package:

        log_pkg.LogPackageAnalyze()
        log_pkg.LogPackageAnalyzerLog("LOG")


    # count = 0
    # for log_pkg in imgLib_startTrace_log_package:
    #     if count % 2 == 0:
    #         log_pkg.LogPackageAnalyze()
    #         log_pkg.LogPackageAnalyzerLog("LOG_L")
    #     elif count % 2 != 0:
    #         log_pkg.LogPackageAnalyze()
    #         log_pkg.LogPackageAnalyzerLog("LOG_U")
    #     count += 1

