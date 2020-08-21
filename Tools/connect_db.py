'''
import pymssql


class OperationMssql:
    def __init__(self):
        self.conn = pymssql.connect(
            host='192.168.1.206',
            user='sa',
            password='sa17track.net',
            database='Test_Deal',
            charset='utf8'
        )

        self.cur = self.conn.cursor()

    def search_one(self, sql):
        self.cur.execute(sql)
        # # 获得查询结果集:
        values = self.cur.fetchone()
        return values


if __name__ == '__main__':
    op_ql = OperationMssql()
    # print(op_ql.search_one("select * from TYQCustomLink where FRemarks ='被禁用'"))
    print(op_ql.search_all("select FPrimaryKeyId from TYQLink order by FPrimaryKeyId offset 0 rows FETCH NEXT 1000 rows only"))

'''

'''
import MySQLdb


class OperationMysql:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='192.168.189.131',
            port=3306,
            user='root',
            passwd='',
            db='test',
            charset='utf8',
            # cursorclass=MySQLdb.cursors.DictCursor
        )
        # self.cur = self.conn.cursor(cursor=MySQLdb.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def search_one(self, sql):
        self.cur.execute(sql)
        # # 获得查询结果集:
        values = self.cur.fetchone()
        # print(values)
        return values


if __name__ == '__main__':
    op_ql = OperationMysql()
    print(op_ql.search_one("select * from TYQCustomLink where FRemarks ='被禁用'"))
'''

# -----------------------------------------------------------------------------------------------


# 导入SQLite驱动

# 连接到SQLite数据库
# 数据库文件是lhrtest.db
# 如果文件不存在，那么会自动在当前目录创建一个数据库文件:

# class OperationSql

import sqlite3, os

current_directory = os.path.dirname(__file__)
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")


class OperationSql:

    def __init__(self):
        self.conn = sqlite3.connect(root_path + '/db.sqlite3')
        # 创建一个Cursor:
        self.cur = self.conn.cursor()

    def search_one(self, sql):
        self.cur.execute(sql)
        # # 获得查询结果集:
        values = self.cur.fetchall()
        # print(values)
        return values
        # # 关闭Cursor:
        # self.cur.close()
        # self.conn.close()


if __name__ == '__main__':
    op_ql = OperationSql()
    print(op_ql.search_one("select * from TYQCustomLink where FRemarks ='被禁用'"))
