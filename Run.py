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
from datetime import datetime
import operationConfig

if __name__ == '__main__':
    setConfig = operationConfig.OperationConfig()
    resports_dir_path = operationConfig.RESPORTS_DIR_PATH
    if not os.path.exists(resports_dir_path):
        os.mkdir(resports_dir_path)
    log_path = os.path.join(resports_dir_path, str(datetime.now().strftime("%Y%m%d%H%M%S")))
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    setConfig.set_report('path', log_path)

    output = os.popen('pytest testCode --html={0}/report.html --json={0}/report.json'.format(log_path))
    print(output.read())
