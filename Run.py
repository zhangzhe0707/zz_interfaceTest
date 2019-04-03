#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author: 

@License: (C) Copyright 2013-2017, 

@Contact: 

@Software: PyCharm

@File: Run.py

@Time: 2019-04-03 08:28

@Desc:

'''

import os
import platform

...

if __name__ == '__main__':
    sysstr = platform.system()
    if (sysstr == "Windows"):
        output = os.popen('pytest testcode --html={0}/report.html'.format("resport"))
        print(output.read())
    elif (sysstr == "Darwin" or sysstr == "Linux" ):
        output = os.popen('pytest testcode --html={0}/report.html'.format("resport"))
        print(output.read())
