import pymysql
from typing import List ,Dict,Tuple
class Datasrc:
    def __init__(self,host,port,user,password,table_name,database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.table_name = table_name
        self.database = database
        self.connection = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,db=self.database)

    def create_table(self, cols:List[Tuple[str, str]]):
        print("============== start create table =============== ")
        with self.connection.cursor() as cursor:
            sql = f"CREATE TABLE IF NOT EXISTS {self.table_name}"
            sql += "("
            for col_name,col_type in cols:
                sql += f"{col_name} {col_type},"
            sql = sql[:-1]
            sql += ")"
            cursor.execute(sql)
        self.connection.commit()

    def insert_into(self,cols:List,values:List,types:list):
        with self.connection.cursor() as cursor:
            sql = f"INSERT INTO {self.table_name} ("
            for col in cols:
                sql += f"{col},"
            sql = sql[:-1]
            sql += ") VALUES ("
            for idx,value in enumerate(values):
                if types[idx] != 'float' or types[idx] != 'int':
                    sql += f"'{value}',"
                else:
                    sql += f"{value},"
            sql = sql[:-1]
            sql += ")"
            print(sql)
            cursor.execute(sql)
        self.connection.commit()

    def clear_table(self):
        with self.connection.cursor() as cursor:
            sql = f"DELETE  from {self.table_name}"
            cursor.execute(sql)
        self.connection.commit()
