#!/usr/bin/python
# coding: utf-8

import pymysql
import time


class TestMysql:
    def __init__(self):
        self.mysql = pymysql

    def connect_mysql(self):
        mysql = self.mysql
        ip = '127.0.0.1'
        port = 3306
        username = 'root'
        password = '123456'
        dbname = 'test_jenkins'
        conn = mysql.Connect(host=ip, user=username, password=password, database=dbname, charset='utf8')
        print("连接数据库")
        return conn

    def mysql_command(self, sql):
        conn = self.connect_mysql()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            print("执行sql失败")
        cursor.close()
        conn.close()


if __name__ == '__main__':
    test = TestMysql()
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sql = 'insert into test set createtime = "{}",title="test_jenkins"'.format(now_time)
    print(sql)
    test.mysql_command(sql)


