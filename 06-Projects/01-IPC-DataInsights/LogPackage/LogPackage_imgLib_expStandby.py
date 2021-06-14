#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ ="Copyright 2021"
__status__ = "Working on deploy Analyzer Design pattern"
__version__ = "2021.06.14"

from LogPackage.LogPackage import *


class LogPackage_imgLib_expStandby (LogPackageAbstract):
    def __init__(self):
        super().__init__()
        self.log_level = ""
        self.log_package_name = "imgLib_expStandby"
        self.log_package_data = ""

    def LogPackageAnalyze(self):
        # for line in self.log_package_data.split("\n")[2:]:
        #     self.log_package_numbers += re.findall(r'[-+]?\d*\.\d+|\d+', ' '.join(line.split()[3:]))
        # return self.log_package_numbers
        for line in self.log_package_data.split("\n"):
            if "TRACELIB" in line:
                if "W:Answer" not in line:
                    self.log_package_numbers += re.findall(r'[-+]?\d*\.\d+|\d+', ' '.join(line.split()[3:]))
        print(self.log_package_numbers)
