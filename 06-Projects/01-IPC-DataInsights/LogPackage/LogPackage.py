#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2021"
__status__ = "Working on deploy Analyzer Design pattern"
__version__ = "2021.06.14"

# Create an abstract Log Package Abstract  class generic for all
# Then create concrete class follow by different in Log Package Data
# Apply the Factory Design Pattern to provide the Log Analyzer the best ways of implementing and manipulating the lgo package

from datetime import datetime
import re
import numpy as np


class LogPackageAbstract:
    def __init__(self):
        # print(datetime.strftime(datetime.now(), "%Y%m%d_%H%M%S.%f") + " " + self.__class__.__name__)
        self.log_level = ""
        self.log_package_name = ""
        self.log_package_data = ""
        self.log_package_numbers = []

        self.log_datetime_info = datetime.strftime(datetime.now(), "%Y%m%d_%H%M%S%f")
        self.log_date_info = datetime.strftime(datetime.now(), "%Y%m%d")

    def LogPackageAnalyze(self):
        pass

    def LogPackageAnalyzerLog(self, log_file_name):
        with open("LogPackageData/" + self.__class__.__name__.upper() + "_" + self.log_date_info + "_" + log_file_name + ".csv", "a") as log_package_data:
            log_package_data.write(",".join(self.log_package_numbers) + "\n")