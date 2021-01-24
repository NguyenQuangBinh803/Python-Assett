#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2020"
__status__ = "Working on deploy stage 2"
__version__ = "2020.10.17"

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            return Singleton()
        else:
            return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance is not None:
            print("Instance has been created!")
        else:
            Singleton.__instance = self
        
        self.x = 1000
        self.y = 1000

    # def __repr__(self):
    #     return ','.join([str(self.x), str(self.y)])

if __name__ == "__main__":
    # singleton = Singleton()
    # print(singleton)
    # print(Singleton.get_instance())
    

    singleton = Singleton.get_instance()
    print(singleton)
    print(Singleton())