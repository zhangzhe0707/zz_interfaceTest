import os
import codecs
import configparser

PROJECT_DIR = os.path.split(os.path.realpath(__file__))[0]
CONFIG_PATH = os.path.join(PROJECT_DIR, 'config', 'config.ini')
RESPORTS_DIR_PATH = os.path.join(PROJECT_DIR, "report")
ENCODING = "UTF-8"


class GetConfig:
    def __init__(self):
        with open(CONFIG_PATH, encoding=ENCODING) as file_object:
            config_data = file_object.read()

            # 移除文件中的BOM BOM = b'\xef\xbb\xbf'
            if config_data[:3] == codecs.BOM_UTF8:
                config_data = config_data[3:]
                with open(CONFIG_PATH, "w", encoding=ENCODING) as file_object:
                    file_object.write(config_data)

            self.config_file = configparser.ConfigParser()
            self.config_file.read(CONFIG_PATH, encoding=ENCODING)

    def get_email(self, name):
        """
        获取 email 相关配置的对应值
        :param self:
        :param name:Email配置关键字名称
        :return:
        """
        value = self.config_file.get("EMAIL", name)
        return value

    def get_http(self, name):
        """
        获取http配置
        :param self:
        :param name: HTTP配置关键字名称
        :return:
        """
        value = self.config_file.get("HTTP", name)
        return value

    def get_db(self, name):
        """
        获取数据库配置
        :param self:
        :param name: DB配置关键字名称
        :return:
        """
        value = self.config_file.get("DATABASE", name)
        return value

    def get_excel(self, name):
        """
        获取Excel字段对应列号
        :param self:
        :param name: Excel 字段列名
        :return:
        """
        value = self.config_file.get("EXCEL", name)
        return value

