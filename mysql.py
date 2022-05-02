"""
mysql.py
pysql 操作基本流程演示
"""

import pymysql

# 鏈接數據庫
db = pymysql.connect(host="localhost",port=3306,user="root",password="a123456",database="stu",charset="utf8")

# 獲取游標(操作數據庫 執行sql語句)
cur = db.cursor()

# 執行sql語句
sql = "insert into class values (6,'Emma',17,'w',79.5,'2019-8-8');"

cur.execute(sql) #執行語句

db.commit() #將寫操作提交 多次寫操作一同提交

# 關閉數據庫
cur.close()
db.close()