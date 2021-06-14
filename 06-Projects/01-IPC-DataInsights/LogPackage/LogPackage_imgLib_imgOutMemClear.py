#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ ="Copyright 2021"
__status__ = "Working on deploy Analyzer Design pattern"
__version__ = "2021.06.14"

from LogPackage.LogPackage import LogPackageAbstract


class LogPackage_imgLib_imgOutMemClear (LogPackageAbstract):
    def __init__(self):
        super().__init__()
        self.log_level = ""
        self.log_package_name = ""
        self.log_package_data = ""

    def LogPackageAnalyze(self):
        pass