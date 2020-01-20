import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import CHAR,INT

def DB_Connect():
    #MySql的用：root 密码：Xfour168*** 端口：3306 数据库：pythonDB
    connect_info = 'mysql+pymysql://root:Xfour168***@localhost:3306/pythonDB?charset=utf8'
    engine = create_engine(connect_info)
    return engine

def ReadAndWriteSQL(engine):
    engine = DB_Connect()
    sql_str = 'SELECT * FROM user;'
    df = pd.read_sql(sql=sql_str,con=engine) #从表中读数据
    print(df)
    df.to_sql(name='test2',con=engine,if_exists='append',index=False,dtype={'id':INT(),'name':CHAR(length=255),'age':INT()}) #把数据存进表中，并创建表
    print(df)

def OpenCSV(csvName):
    engine = DB_Connect()
    df = pd.read_csv(csvName)
    # print(df.head()) #打印前五行
    # print(df.tail()) #打印后五行
    # print(df.ix[0:10,0:2])
    df.to_sql('panda',engine,if_exists='append',index=False) #把数据存进表


def main():
    OpenCSV('PandaTest.csv')
    # ReadAndWriteSQL()

main()