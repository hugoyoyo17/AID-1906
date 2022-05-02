"""
read_db.py
"""

import pymysql

# 鏈接數據庫
db = pymysql.connect(host="localhost",port=3306,user="root",password="a123456",database="stu",charset="utf8")

# 獲取游標(操作數據庫 執行sql語句)
cur = db.cursor()

# 執行sql語句
sql = "select * from class where gender = 'm';"

cur.execute(sql) #執行正確後cur調用函數獲取結果

# 獲取一個查詢結果
# one_row = cur.fetchone()
# print(one_row) #元組

# 獲取多個查詢結果
# many_row = cur.fetchmany(2)
# print(many_row)

# 獲取所有查詢結果
all_row = cur.fetchall()
print(all_row)


# 關閉數據庫
cur.close()
db.close()