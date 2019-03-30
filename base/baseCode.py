import os
import json
import getConfig


class BaseCode:

    def __init__(self):
        self.LOCAL_READ_CONFIG = getConfig.GetConfig()
        self.PRO_DIR = getConfig.PROJECT_DIR

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


