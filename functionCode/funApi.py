#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author: zz

@License: (C) Copyright 2013-2017, 

@Contact: 

@Software: PyCharm

@File: funApi.py

@Time: 2019-03-20 21:32

@Desc:  框架逻辑类库

'''

import os
from base.baseExcel import BaseExcel
from base.baseHttp import BaseHttp
from base.baseDB import BaseDB
from base.log import Log
import getConfig


class FunApi:
    def __init__(self):
        log = Log()
        locals_get_config = getConfig.GetConfig()
        self.case_no = locals_get_config.get_excel("case_no")
        self.case_name = locals_get_config.get_excel("case_name")
        self.case_front_sql = locals_get_config.get_excel("case_front_sql")
        self.case_data = locals_get_config.get_excel("case_data")
        self.case_uri = locals_get_config.get_excel("case_uri")
        self.case_method = locals_get_config.get_excel("case_method")
        self.case_code = locals_get_config.get_excel("case_code")
        self.case_result = locals_get_config.get_excel("case_result")
        self.excel_path = os.path.join(getConfig.PROJECT_DIR, locals_get_config.get_excel("excel_file"))
        self.logger = log.get_logger()

    def prepare_data(self, sql):
        """
        数据准备，添加测试数据
        :param sql:SQL命令
        :return:
        """
        db = BaseDB()
        res = db.excuteSql(sql)
        db.closeDb()
        self.logger.info("执行SQL结果:{0}".format(res))

    def run_test(self, sheet_name):
        """
        执行测试用例
        :param sheet:
        :return:
        """
        http = BaseHttp()
        excel = BaseExcel(self.excel_path)
        rows = excel.get_rows(sheet_name)
        # 遍历执行测试用例
        for i in range(1, rows):
            # 获取测试数据
            test_name = excel.get_content(sheet_name, i, self.case_name)
            test_front_sql = excel.get_content(sheet_name, i, self.case_front_sql)
            test_case_uri = excel.get_content(sheet_name, i, self.case_uri)
            test_case_data = excel.get_content(sheet_name, i, self.case_data)
            test_case_method = excel.get_content(sheet_name, i, self.case_method)
            test_case_code = excel.get_content(sheet_name, i, self.case_code)

            # 执行接口测试
            self.logger.info("---------CaseName:{0} START--------".format(test_name))
            # 处理前置数据
            if test_front_sql:
                self.prepare_data(test_front_sql)

            if test_case_method == "get":
                action_response = http.get(test_case_uri, test_case_data)
                self.logger.info("get请求返回结果:%s" % action_response)
            elif test_case_method == "post":
                action_response = http.post_with_json(test_case_uri, test_case_data)
                self.logger.info("post请求返回结果:%s" % action_response)
            else:
                action_response = None
            actualCode = int(action_response.status_code)

            if actualCode != test_case_code:
                excel.set_countent(sheet_name, i, self.case_result, "Fail")
            else:
                excel.set_countent(sheet_name, i, self.case_result, "Pass")

            self.logger.info("---------CaseName:{0} END--------".format(test_name))
