from datetime import datetime

import pymysql


# DATABASE_URI = ("mysql+pymysql://root:@Yong6457493@8.129.86.105:3306/student?charset=utf8mb4")

class MysqlOperate:

    def __init__(self):
        self.host = "139.9.0.72"
        self.db = None
        self.port = 32306
        self.user = "root"
        self.password = "Zp1234!@#$"
        self.conn = None
        self.cur = None

    def __conn_db(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                port=self.port,
                charset="utf8"
            )
        except Exception as e:
            print(e)
            return False
        self.cur = self.conn.cursor()
        return True

    def __close_conn(self):
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        self.conn.commit()
        return True

    def query(self, sql):

        self.__conn_db()
        self.cur.execute(sql)
        query_data = self.cur.fetchall()
        if query_data == ():
            query_data = None
            print("没有获取到数据")
        else:
            pass
        self.__close_conn()

        return query_data

    def insert_update_table(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        self.__commit()
        self.__close_conn()


import json
from datetime import datetime
from decimal import Decimal

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, Decimal):
            return float(o)  # 将 Decimal 转换为 float 类型
        return super().default(o)


if __name__ == '__main__':
    sql = "select * from edu_pm.epm_position_info limit 0,10"
    result = MysqlOperate().query(sql)
    print(result)

