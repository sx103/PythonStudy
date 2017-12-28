#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:19:23 2017

@author: kenneth.shu
"""

''''
import sys

print('The command line arguments are:')

for i in sys.argv:
    print(i)
'''

import test_module_2

from test_module_2 import saySth
print("use from...import to execute saySth function")
saySth()
print("the version of module 2 is ", test_module_2.__version__)
print("the doc of module 2 is ", test_module_2.__doc__)
print("Executing the dir function.")
print(dir())
print(dir(test_module_2))
