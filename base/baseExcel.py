#!/usr/bin/env python

# -*- encoding: utf-8 -*-

"""
@Author: zz

@License: (C) Copyright 2013-2017, haima

@Contact :   

@Software: PyCharm

@File: baseExcel.py

@Time: 2019-03-19 23:50

@Desc:

"""

import xlrd
from xlutils3.copy import copy
from base.log import Log


class BaseExcel:
    """
        Excel请求封装类
    """

    def __init__(self, path):
        self.path = path
        log = Log()
        self.logger = log.get_logger()
        try:
            self.workbook = xlrd.open_workbook(self.path, on_demand=True)
        except BaseException as e:
            self.logger.error("打开 Excel 文件失败：%s" % e)

    def get_sheet(self, sheet_name):
        """
        获取sheet
        :param sheet_name: 表单名
        :return:
        """
        try:
            sheet = self.workbook.sheet_by_name(sheet_name)
        except BaseException as e:
            self.logger.error("打开 Sheet失败失败：%s" % e)
        return sheet


    def get_sheetnames(self):
        """
        获取所有sheet
        :param sheet_name: 表单名
        :return:
        """
        return self.workbook.sheet_names()

    def get_rows(self, sheet_name):
        """
        获取行号
        :return:
        """
        sheet = self.get_sheet(sheet_name)
        return sheet.nrows

    def get_cols(self, sheet_name):
        """
        获取列号
        :return:
        """
        sheet = self.get_sheet(sheet_name)
        return sheet.ncols

    def get_content(self, sheet_name, row, col):
        """
        获取表格中内容
        :param row:行
        :param col:列
        :return:s
        """
        sheet = self.get_sheet(sheet_name)
        cell_value = sheet.cell_value(int(row), int(col))
        if type(cell_value) == float:
            return int(cell_value)
        return cell_value

    def release(self):
        """
        释放 excel 对象
        :return:
        """
        self.workbook.release_resources()

    def get_sheetindex(self, sheet_name):
        sheet_names = self.get_sheetnames()
        for index, value in enumerate(sheet_names):
            if sheet_name == value:
                return index
        return None

    def set_countent(self, sheet_name, row, col, cell_value):
        """
        写入指定单元格内容
        :param row:
        :param col:
        :return:
        """
        wb = copy(self.workbook)
        sheet_index = self.get_sheetindex(sheet_name)
        sheet = wb.get_sheet(sheet_index)

        sheet.write(row, col, cell_value)
        wb.save(self.path)


# if __name__=="__main__":
#     be = BaseExcel("/Users/zhezhang/Code/PythonPractice/zz_InterfaceTest/TestCase/testcase.xls")
#     print(be.get_rows("TestCase_bak"))
#     print(be.get_cols("TestCase_bak"))
#     print(be.get_content("TestCase_bak",3,4))
#     print(be.get_sheetnames())
#     print(be.get_sheetindex("TestCase_bak"))
#     be.set_countent("工作表1",1,2,"test接口测试")
#     be.release()