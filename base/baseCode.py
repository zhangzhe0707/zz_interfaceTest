import os
import json
import operationConfig
from base.log import Log
from base.baseExcel import BaseExcel


class BaseCode:

    def __init__(self):
        log = Log()
        self.LOCAL_READ_CONFIG = operationConfig.OperationConfig()
        self.PRO_DIR = operationConfig.PROJECT_DIR
        self.logger = log.get_logger()

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

    def get_case_data(self, sheet_name, method_type="all", rowNubmer=None):
        """
        获取Excel 中的接口测试用例数据
        :param sheet_name:
        :return:
        """
        locals_get_config = operationConfig.OperationConfig()

        case_data = []
        excel_file = BaseExcel(os.path.join(self.PRO_DIR, self.LOCAL_READ_CONFIG.get_excel("excel_file")))

        # 获取行数
        nrows = excel_file.get_rows(sheet_name)

        # 判断是不是指定行号获取数据
        if rowNubmer == None:
            for i in range(1, nrows):
                test_no = excel_file.get_content(sheet_name, i, locals_get_config.get_excel("case_no"))
                test_name = excel_file.get_content(sheet_name, i, locals_get_config.get_excel("case_name"))
                test_front_sql = excel_file.get_content(sheet_name, i, locals_get_config.get_excel("case_front_sql"))
                test_case_uri = excel_file.get_content(sheet_name, i, locals_get_config.get_excel("case_uri"))
                test_case_data = excel_file.get_content(sheet_name, i, locals_get_config.get_excel("case_data"))
                test_case_method = excel_file.get_content(sheet_name, i, locals_get_config.get_excel("case_method"))
                test_case_code = excel_file.get_content(sheet_name, i, locals_get_config.get_excel("case_code"))
                if method_type == "all":
                    case_dict = {'caseNo': test_no, 'caseName': test_name, 'caseFrontSQL': test_front_sql,
                                 "caseUri": test_case_uri,
                                 "caseData": test_case_data, "caseMethod": test_case_method,
                                 "caseStatusCode": test_case_code}
                    case_data.append(case_dict)
                    self.logger.info("测试用例{0}完成测试数据读取.".format(test_name))
                elif method_type == test_case_method:
                    case_dict = {'caseNo': test_no, 'caseName': test_name, 'caseFrontSQL': test_front_sql,
                                 "caseUri": test_case_uri,
                                 "caseData": test_case_data, "caseMethod": test_case_method,
                                 "caseStatusCode": test_case_code}
                    case_data.append(case_dict)
                    self.logger.info("测试用例{0}完成测试数据读取.".format(test_name))

        elif rowNubmer > 0:
            test_no = excel_file.get_content(sheet_name, rowNubmer, locals_get_config.get_excel("case_no"))
            test_name = excel_file.get_content(sheet_name, rowNubmer, locals_get_config.get_excel("case_name"))
            test_front_sql = excel_file.get_content(sheet_name, rowNubmer,
                                                    locals_get_config.get_excel("case_front_sql"))
            test_case_uri = excel_file.get_content(sheet_name, rowNubmer, locals_get_config.get_excel("case_uri"))
            test_case_data = excel_file.get_content(sheet_name, rowNubmer, locals_get_config.get_excel("case_data"))
            test_case_method = excel_file.get_content(sheet_name, rowNubmer, locals_get_config.get_excel("case_method"))
            test_case_code = excel_file.get_content(sheet_name, rowNubmer, locals_get_config.get_excel("case_code"))
            case_dict = {'caseNo': test_no, 'caseName': test_name, 'caseFrontSQL': test_front_sql,
                         "caseUri": test_case_uri,
                         "caseData": test_case_data, "caseMethod": test_case_method,
                         "caseStatusCode": test_case_code}
            case_data.append(case_dict)
            self.logger.info("测试用例{0}完成测试数据读取.".format(test_name))
        return case_data
