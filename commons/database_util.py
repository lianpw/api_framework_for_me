"""
@Filename:  commons/database_util
@Author:   lianpengwei
@Time:    2022/6/21 17:16
@Describe:  ...
"""
import pymysql


class DatabaseUtil:

    conn = None

    # 获取连接对象
    @classmethod
    def get_conn(cls):
        if cls.conn is None:
            cls.conn = pymysql.connect(host='rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com',
                port=3306,
                database='wm_sharing_platform',
                user='web_user',
                password='l%meFN!Z88yRgrjz',
                charset='utf8')
        return cls.conn

    # 获取游标对象
    @classmethod
    def get_cursor(cls):
        return cls.get_conn().cursor()

    # 关闭游标对象
    @classmethod
    def close_cursor(cls, cursor):
        if cursor:
            cursor.close()

    # 关闭连接对象
    @classmethod
    def close_conn(cls):
        if cls.conn:
            cls.conn.close()
            cls.conn = None

    # 获取一条数据
    @classmethod
    def get_sql_one(cls, sql):
        cursor = cls.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cls.close_cursor(cursor)
        cls.close_conn()
        return data

    # 获取所有结果集
    @classmethod
    def get_sql_all(cls, sql):
        cursor = cls.get_cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cls.close_cursor(cursor)
        cls.close_conn()
        return data