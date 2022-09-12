from typing import List
import pymysql

con = pymysql.connect(host='db', user='root', password='example',
                       db='kwu_readingroom', charset='utf8',autocommit=True)


cur = con.cursor()

def create_table():
    sql = '''CREATE TABLE user ( 
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    email varchar(255), 
    department varchar(255) 
    ) 
    ''' 

def write_seats(room_num : int, table_num : List[int]):
    pass

