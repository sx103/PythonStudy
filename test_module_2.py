#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:33:31 2017

@author: kenneth.shu
"""


def saySth():
    """ this is a function to test the __name__ and ___version__ """
    print("The saySth function is executing.")
    print("The __name__ is ", __name__)


__version__ = "0.2"
