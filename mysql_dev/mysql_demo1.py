﻿import pymysql

host = '127.0.0.1'
port = 3306
db = ''
user = 'root'
password = 'root'

def get_connection():
    conn = pymysql.connect(host=host,port=port,db=db,user=user,password=password,charset='utf-8')
    return conn


def check_it():

    conn = get_connection()

    # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select count(id) as total from Product")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("-- 当前数量: %d " % data['total'])

    # 关闭数据库连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    check_it()