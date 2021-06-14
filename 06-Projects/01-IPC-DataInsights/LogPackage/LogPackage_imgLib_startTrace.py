#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2021"
__status__ = "Working on deploy Analyzer Design pattern"
__version__ = "2021.06.14"

from LogPackage.LogPackage import *


class LogPackage_imgLib_startTrace(LogPackageAbstract):
    def __init__(self):
        super().__init__()
        self.log_package_name = "imgLib_startTrace"

    def LogPackageAnalyze(self):
        for line in self.log_package_data.split("\n")[2:]:
            self.log_package_numbers += re.findall(r'[-+]?\d*\.\d+|\d+', ' '.join(line.split()[3:]))
        return self.log_package_numbers


