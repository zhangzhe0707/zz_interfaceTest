import os
import json
import getConfig
from base.log import Log
from base.baseExcel import BaseExcel


class BaseCode:

    def __init__(self):
        log = Log()
        self.LOCAL_READ_CONFIG = getConfig.GetConfig()
        self.PRO_DIR = getConfig.PROJECT_DIR
        self.logger = log.get_logger()
        self.case_No = 0

    def get_value_from_return_json(json, value1, value2):
        """
        get value by key
        :param json:
        :param value1:
        :param value2:
        :return:
        """
        info = json['info']
        group = info[value1]
        value = group[value2]

        return value

    def show_retrun_msg(self, response):
        """
        输出response中 msg 信息
        :param response:
        :return:
        """
        url = response.url
        msg = response.text

        print("请求地址:{0}".format(url))
        print("请求返回值:{0}".format(json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4)))

    def get_test_case_path(self):
        return os.path.join(self.PRO_DIR, self.LOCAL_READ_CONFIG.get_excel("excel_file"))

    def get_case_data(self, sheet_name):
        """
        获取Excel 中的接口测试用例数据
        :param sheet_name:
        :return:
        """
        locals_get_config = getConfig.GetConfig()

        case_dict = {}
        excel_file = BaseExcel(self.get_test_case_path)
        # 获取指定 sheet数据
        sheet = excel_file.get_sheet(sheet_name)
        # 获取行数
        nrows = excel_file.get_rows(sheet_name)
        # 获取列号
        ncols = excel_file.get_cols(sheet_name)

        for i in range(nrows):
            test_name = excel_file.get_content(sheet_name, i, self.case_name)
            test_front_sql = excel_file.get_content(sheet_name, i, self.case_front_sql)
            test_case_uri = excel_file.get_content(sheet_name, i, self.case_uri)
            test_case_data = excel_file.get_content(sheet_name, i, self.case_data)
            test_case_method = excel_file.get_content(sheet_name, i, self.case_method)
            test_case_code = excel_file.get_content(sheet_name, i, self.case_code)
            case_data = {'caseName': test_name, 'caseFrontSQL': test_front_sql, "caseUri": test_case_uri,
                         "caseData": test_case_data,""}
