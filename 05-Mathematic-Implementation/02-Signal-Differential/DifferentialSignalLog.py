#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2021"
__status__ = "Created"
__version__ = "2021.04.22"

from datetime import datetime


class Log:
    def __init__(self):
        pass

    def log(self, scope_name, log_string):
        print("[LOGGING] [" + datetime.strftime(datetime.now(), "%y%m%d_%H%M%S") + "] " + "[" + scope_name + "] " + "[" + log_string + "]")
