import os
import logging
from datetime import datetime
import getConfig

LOCAL_READ_CONFIG = getConfig.GetConfig()
ENCODING = 'UTF-8'


class Log:
    def __init__(self):
        # project_dir = getConfig.PROJECT_DIR
        resports_dir_path = getConfig.RESPORTS_DIR_PATH
        if not os.path.exists(resports_dir_path):
            os.mkdir(resports_dir_path)
        log_path = os.path.join(resports_dir_path, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        # 定义 logger 实例
        self.logger = logging.getLogger()

        # 定义日志级别
        self.logger.setLevel(logging.INFO)

        # 定义日志路径默认
        defaulthandler = logging.FileHandler(os.path.join(log_path, "output.log"), encoding=ENCODING)

        # 定义默认日志的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        defaulthandler.setFormatter(formatter)

        # 给logger实例添加handler
        self.logger.addHandler(defaulthandler)

    def get_logger(self):
        """
        获取log 日志
        :return:
        """
        return self.logger

    def add_start_line(self, case_no):
        """
        写入开启记录日志标识行
        :param case_no:
        :return:
        """
        self.logger.info("---------CaseName:{0} START--------".format(case_no))

    def add_end_line(self, case_no):
        """
        写入结束记录日志标识行
        :param case_no:
        :return:
        """
        self.logger.info("---------CaseName:{0} END--------".format(case_no))

