#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2021"
__status__ = "Working on deploy Analyzer Design pattern"
__version__ = "2021.06.14"

# Just a little feelings but why I keep unsatisfied with this design
# May be because of the number of concrete class required is too much
from LogPackage import *
from datetime import datetime


class LogPackageFactory:
    def __init__(self):
        print(datetime.strftime(datetime.now(), "%Y%m%d_%H%M%S.%f") + " " + self.__class__.__name__)

    def FactoryProduce(self, log_package_type):
        # Tis is the most cost effective design ever made by Edward, however the drawbacks remains to be a bunch of secufrity flaws
        try:
            return eval("LogPackage_" + log_package_type)()
        except NameError as exp:
            print(datetime.strftime(datetime.now(), "%Y%m%d_%H%M%S.%f") + " " + self.__class__.__name__ + " " + str(exp))
            #     Create new instance
            with open("LogPackage/LogPackage_" + log_package_type + ".py", "w") as instance_file:
                instance_file.write(LogPackageInstanceTemplate % log_package_type)
            with open("LogPackage/__init__.py", "a") as instance_file:
                instance_file.write("from LogPackage.LogPackage_%s import *" % log_package_type + "\n")

            # After creation reimport the module
            exec("from LogPackage." + "LogPackage_" + log_package_type + " import " + "LogPackage_" + log_package_type)
            # exec("from LogPackage import *")
            return eval("LogPackage_" + log_package_type)()


if __name__ == "__main__":
    log_package_factory = LogPackageFactory()
    log_package = log_package_factory.FactoryProduce("TrexACL_clearImageBuffer")
    print(log_package.log_package_name)
