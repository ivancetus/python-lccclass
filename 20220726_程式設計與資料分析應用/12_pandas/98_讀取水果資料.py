# 當資料庫欄位設定好, 發布了, 就不准再變更
# 資料庫以日記帳設計
# 資料呈現用樞紐分析表, 可以用資料庫的功能, python去轉換

import mysql.connector as mysql
conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")
cursor=conn.cursor()
cmd="select * from fruit"
cursor.execute(cmd)
data=[]
for r in cursor.fetchall():
    data.append([str(r[1]),r[2],r[3],r[4],r[5]])
cursor.close()
conn.close()

# print(data)

conn=mysql.connect(host='localhost',
                   user='dengfixanros',
                   password='666x-GGteng%',
                   database='cloud')
cursor=conn.cursor()
cmd="insert into 水果銷售 (日期, 國家, 水果, 數量, 單價) values (%s, %s, %s, %s, %s)"
cursor.executemany(cmd,data)
conn.commit()
cursor.close()
conn.close()