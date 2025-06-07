import pymysql
from timeit import default_timer
def get_connection():
    conn = pymysql.connect(host=host,port=port,db=db,user=user,password=password,charset='utf-8')
    return conn

class MySQLContext():
    def __init__(self,commit=True,log_time=True,log_label="总用时:"):
        self._log_time = log_time
        self._commit = commit
        self._log_label = log_label

    def __enter__(self):
        if self._log_time is True:
            self._start = default_timer
        conn = get_connection()
        cursor  =conn.cursor(pymysql.cursors.DictCursor)
        conn.autocommit = False

        self._conn = conn
        self._cursor = cursor
        return self
    def __exit__(self,*exec_info):
        if self._commit:
            self.__conn.commit()
        self._cursor.close()
        self._conn.close()

        if self._log_time is True:
            diff = default_timer() - self._start
            print('-- %s: %.6f 秒' % (self._log_label, diff))
