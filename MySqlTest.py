import pymysql as sql
import string
import random

class MySQLConfig:
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = 'Xfour168***' 
    DB_Name = 'pythonDB'
    charset = 'utf8'


sql_config = MySQLConfig()

def Connect_DB(db_name):
    conn = sql.connect(sql_config.host,user=sql_config.user,passwd=sql_config.passwd)
    conn.select_db(db_name)
    cursor = conn.cursor()
    return conn,cursor

#创建数据库
def Create_DB():
    conn = sql.connect(sql_config.host,user=sql_config.user,passwd=sql_config.passwd)
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS pythonDB DEFAULT CHARSET utf8')
    print("Create_DB Succeed")
    cursor.close()
    conn.close()

#创建表
def Create_Table(db_name):
    conn,cursor = Connect_DB(db_name)
    cursor.execute('drop table if exists user')
    sql_str = """CREATE TABLE IF NOT EXISTS `user` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL,
        `age` int(11) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

        #注意这个标点符号 ` ,其他的会报错 '
    cursor.execute(sql_str)
    cursor.close()
    conn.close()
    print("Create_Table Succeed")

#往表中插入数据
def Insert_Data(db_name):
    Create_Table(db_name)
    conn,cursor = Connect_DB(db_name)
    #方式一
    # insert = cursor.execute("insert into user values(1,'tom',18)")
    # print(insert)
    #方式二
    insert_str = "insert into user values(%s,%s,%s)"
    # cursor.execute(insert_str,(2,'kongsh',20))

    #同时插入多条数据
    # cursor.executemany(insert_str,[(3,'joker',15),(4,'tom',16),(5,'test',40)])

    #往表中插入一百条数据
    words = list(string.ascii_letters)
    # for i in range(100):
    #     random.shuffle(words)#打乱顺序
    #     cursor.execute(insert_str,(i+1,''.join(words[:5]),random.randint(0,80)))

    #一次插入多条
    cursor.executemany(insert_str,[(i+1,''.join(words[:5]),random.randint(0,80)) for i in range(100) ])

    #插入100条数据后查询所有
    cursor.execute("select * from user;")
    for res in cursor.fetchall():
        print(res)

    cursor.close()
    conn.commit()
    conn.close()
    print("Insert_DATA Succeed")

#查表中数据
def Check_Table_Data(db_name):
    conn,cursor = Connect_DB(db_name)
    cursor.execute("select * from user;")
    while 1:
        res = cursor.fetchone()
        if res is None:
            #已经从表中取完结果
            break
        print(res)

    check_str = "select * from user"
    #取所有数据
    cursor.execute(check_str)
    print(cursor.fetchall())
    #取固定几条
    cursor.execute(check_str)
    resTuple = cursor.fetchmany(3)
    print(resTuple)
    #显示数组条数
    print(cursor.arraysize)
    cursor.close()
    conn.commit()
    conn.close()
    print("Check_Table_Data Succeed")

#表中更新数据
def Update_Table_Data(db_name):
    conn,cursor = Connect_DB(db_name)
    upadte = cursor.execute("update user set age=55 where name='tom'")
    print("修改的行数: ",upadte)
    cursor.execute('select * from user where name="tom";')
    print(cursor.fetchone())

    #更新前查询数据
    cursor.execute("select * from user where name in ('kongsh','joker');")
    for res in cursor.fetchall():
        print(res)
    print('*'*40)
    #更新2条数据
    str1 = "update user set age=%s where name=%s"
    update_str = cursor.executemany(str1,[(15,'kongsh'),(18,'joker')])

    #更新后查询
    cursor.execute("select * from user where name in ('kongsh','joker');")
    for res in cursor.fetchall():
        print(res)

    cursor.close()
    conn.commit()
    conn.close()
    print("Update_Table_Data Succeed")

#删除表中数据
def Delete_Table_Data(db_name):
    conn,cursor = Connect_DB(db_name)
    #删除前查询所有数据
    cursor.execute("select * from user;")
    for res in cursor.fetchall():
        print(res)
    print('*'*40)
    #删除一条数据
    cursor.execute("delete from user where id=1")

    #删除后查询
    cursor.execute("select * from user;")
    for res in cursor.fetchall():
        print(res)

    #删除2条数据
    str2 = "delete from user where id=%s"
    cursor.executemany(str2,[(2),(5)])
    print('*'*40)
    #删除后查询
    cursor.execute("select * from user;")
    for res in cursor.fetchall():
        print(res)

    print('*'*40)
    #回滚事物
    conn.rollback()
    cursor.execute("select * from user;")
    for res in cursor.fetchall():
        print(res) 

    cursor.close()
    conn.commit()
    conn.close()
    print("Delete_Table_Data Succeed")

#求该列的平均值
def Avg_Table(db_name):
    conn,cursor = Connect_DB(db_name)
    avg_str = 'SELECT AVG(age) AS age FROM user;'
    cursor.execute(avg_str)
    result = cursor.fetchone() #fetchone 返回一个结果 fetchall 返回所有结果 fetchmany(size) 返回前几个结果
    print(result)

#查询表中条件行的数目
def Count_Table(db_name):
    conn,cursor = Connect_DB(db_name)
    count_str = 'SELECT COUNT(*) AS age FROM user;' #*对所有行计数
    cursor.execute(count_str)
    result = cursor.fetchone()
    print(result)

#查询指定列中最大值
def MAX_Table(db_name):
    conn,cursor = Connect_DB(db_name)
    max_str = 'SELECT MAX(age) AS age FROM user;'
    cursor.execute(max_str)
    result = cursor.fetchone()
    print(result)

#查询指定列中最小值
def MIN_Table(db_name):
    conn,cursor = Connect_DB(db_name)
    min_str = 'SELECT MIN(age) AS age FROM user;'
    cursor.execute(min_str)
    result = cursor.fetchone()
    print(result)

#查询指定列中所有数的和
def SUM_Table(db_name):
    conn,cursor = Connect_DB(db_name)
    sum_str = 'SELECT SUM(age) AS age FROM user;'
    cursor.execute(sum_str)
    result = cursor.fetchone()
    print(result)

def main():
    # Insert_Data(sql_config.DB_Name)
    # Check_Table_Data(sql_config.DB_Name)
    # Update_Table_Data(sql_config.DB_Name)
    # Delete_Table_Data(sql_config.DB_Name)
    # Avg_Table(sql_config.DB_Name)
    # Count_Table(sql_config.DB_Name)
    # MAX_Table(sql_config.DB_Name)
    # MIN_Table(sql_config.DB_Name)
    SUM_Table(sql_config.DB_Name)


if __name__=='__main__':
    main()