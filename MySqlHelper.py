import pymysql as sql
import LoggerHelper
import string
import random

class MySQLConfig:
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = 'Xfour168***' 
    DB_Name = 'PythonDB'
    charset = 'utf8'

sql_config = MySQLConfig()
logger = LoggerHelper.Logger('DBLog.log')

class DBHelper(object):
    def __init__(self,sql,params=None):
        self.sql = sql
        self.params = params
        self.conn = None
        self.cur = None

    def connectdatabase(self):
        logger.Log('host = %s, user = %s, passwd = %s' % (sql_config.host,sql_config.user,sql_config.passwd))
        try:
            self.conn = sql.connect(sql_config.host,sql_config.user,sql_config.passwd,sql_config.DB_Name)
        except:
            logger.Error('connectDatabase failed')
            return False
        self.cur = self.conn.cursor()
        return True

    def closedatabase(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    #执行sql语句  单操作
    def execute(self):
        self.connectdatabase()
        try:
            if self.conn and self.cur:
                self.cur.execute(self.sql,self.params)
                self.conn.commit()
        except:
            logger.Error('execute failed: ' + self.sql)
            logger.Error('params: ' + self.params)
            self.closedatabase()
            return False
        return True
    
    #执行sql语句 多操作
    def executemany(self):
        self.connectdatabase()
        try:
            if self.conn and self.cur:
                self.cur.executemany(self.sql,self.params)
                self.conn.commit()
        except:
            logger.Error('executemany failed: ' + self.sql)
            logger.Error('params: ' + self.params)
            self.closedatabase()
            return False
        return True

    #查询表数据
    def select(self):
        self.connectdatabase()
        try:
            self.cur.execute(self.sql,self.params)
            result = self.cur.fetchall()
            logger.Log(result)
            return result
        except:
            logger.Error('select failed: ' + self.sql)
            logger.Error('params: ' + self.params)
            self.closedatabase()
            return False


def main():
    #删除表 test
    dbHelper = DBHelper("drop table if exists test")
    dbHelper.execute()

    #创建表 test
    sql_str = """CREATE TABLE IF NOT EXISTS `test` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL,
        `age` int(11) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
    dbHelper = DBHelper(sql_str)
    dbHelper.execute()
    
    #插入数据
    insert_str = "insert into test values(%s,%s,%s)"
    dbHelper = DBHelper(insert_str,(2,'kongsh',20))
    dbHelper.execute()
    #查询是否插入成功
    dbHelper = DBHelper("select * from test where name='kongsh'")
    dbHelper.select()
   
    #更新数据
    update_str = "update test set age=55 where name='kongsh'"
    dbHelper = DBHelper(update_str)
    dbHelper.execute()
    #查询是否更新成功
    dbHelper = DBHelper("select * from test where name='kongsh'")
    dbHelper.select()

    #删除数据
    dbHelper = DBHelper("delete from test where name='kongsh'")
    dbHelper.execute()
    #查询是否删除成功
    dbHelper = DBHelper("select * from test where name='kongsh'")
    dbHelper.select()

    #一次插入多条
    words = list(string.ascii_letters)
    dbHelper = DBHelper(insert_str,[(i+1,''.join(words[:5]),random.randint(0,80)) for i in range(100) ])
    dbHelper.executemany()
    #查询所有数据
    dbHelper = DBHelper("select * from test")
    dbHelper.select()

    #查列中平均值
    dbHelper = DBHelper("SELECT AVG(age) AS age FROM test;")
    dbHelper.select()

    #查询指定列的数目
    dbHelper = DBHelper("SELECT COUNT(age) AS age FROM test;")
    dbHelper.select()

    #查询指定列最大值
    dbHelper = DBHelper("SELECT MAX(age) AS age FROM test;")
    dbHelper.select()

    #查询指定列最小值
    dbHelper = DBHelper("SELECT MIN(age) AS age FROM test;")
    dbHelper.select()

    #查询指定列值的和
    dbHelper = DBHelper("SELECT SUM(age) AS age FROM test;")
    dbHelper.select()

    dbHelper.closedatabase()

main()