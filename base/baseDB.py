import pymysql
import getConfig as getConfig
from base import Log

localsGetConfig = getConfig.GetConfig()


class BaseDB:
    """
    框架操作Mysql的功能封装
    """

    def __init__(self):
        log = Log()
        self.host = localsGetConfig.get_db("host")
        self.username = localsGetConfig.get_db("username")
        self.password = localsGetConfig.get_db("password")
        self.port = localsGetConfig.get_db("port")
        self.database = localsGetConfig.get_db("database")
        self.config = {
            'host': self.host,
            'user': self.username,
            'password': self.password,
            'port': int(self.port),
            'db': self.database,
            'charset': 'utf8'
        }
        self.log = log.get_logger()
        self.db = None
        self.cursor = None

    def connectDb(self):
        """
        连接数据库
        :param self:
        :return:
        """

        try:
            self.db = pymysql.connect(**self.config)
            self.cursor = self.db.cursor()
            self.log.info("数据库连接成功!")
        except ConnectionError as ex:
            self.log.error(str(ex))

    def excuteSql(self, sql):
        """
        执行 SQL命令
        :param sql:
        :param params:
        :return:
        """
        self.connectDb()
        self.cursor.execute(sql)
        self.db.commit()
        self.log.info("执行SQL命令为:{0}".format(sql))
        return self.cursor

    def get_all_data(self, cursor):
        """
        获取执行 SQL所有结果数据
        :param cursor:
        :return:
        """
        data = cursor.fetchall()
        self.log.info("执行数据库查询的结果所有数据:{0}".format(data))
        return data

    def get_one_data(self, cursor):
        """
        获取执行 SQL结果的首行数据
        :param cursor:
        :return:
        """
        data = cursor.fetchone()
        self.log.info("执行数据库查询的结果单行数据:{0}".format(data))
        return data

    def get_row_data(self, cursor, rows):
        """
        获取执行 SQL结果的指定前n行数据
        :param cursor:
        :param rows:返回指定数据的行数
        :return:
        """
        data = cursor.fetchmany(rows)
        self.log.info("执行数据库查询的结果指定前{0}行数据:{1}".format(rows, data))
        return data

    def closeDb(self):
        """
        关闭数据库连接
        :return:
        """
        self.cursor.close()
        self.db.close()
        self.log.info("数据库连接关闭!")


