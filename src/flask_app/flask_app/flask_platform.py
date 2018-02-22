#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:11:16 2018

@author: sam
"""

import systeminfo

def main():
    output = systeminfo.get_platform()
    print(output)
    return