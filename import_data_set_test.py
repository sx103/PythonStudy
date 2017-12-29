#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:14:11 2017

The scripts in this file is to load two columns (numbers) from a CSV file and compare the difference
between the values in the two columnes.

@author: kenneth.shu
"""

import pandas as pd
import math as math
#import numpy as mp

def removeNaN(alist):
    result_list = []
    for item in alist:
        if not math.isnan(item):
            result_list.append(int(item))
    return result_list
#end of function

#import the the data
print('importing the data file')
dataset = pd.read_csv('./set_test_1.csv')

col1 = dataset.iloc[:, 1].values
col2 = dataset.iloc[:, 2].values

print('The column one data is as below.')
print(len(col1))
print(col1)
print('The column two data is as below.')
print(len(col2))
print(col2)

print("Remove all nan from the list")
col1_list = list(col1)
col2_list = list(col2)

col1_list_nd = removeNaN(col1_list)
col2_list_nd = removeNaN(col2_list)

print(len(col1_list_nd))
print(col1_list_nd)
print(len(col2_list_nd))
print(col2_list_nd)

print("Convert to set object")
set1 = set(col1_list_nd)
set2 = set(col2_list_nd)
print(len(set1))
print(set1)
print(len(set2))
print(set2)
print("\n")
print('In both sets : {}'.format(set1 & set2))
print('In Set1 but not in Set2 :{}'.format(set1 - set2))
print('In Set2 but not in Set1 :{}'.format(set2 - set1))
