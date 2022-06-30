import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python', db='python', charset='utf8')

cur = conn.cursor()

sql = "select * from emp"
cur.execute(sql)

rows = cur.fetchall()
print(rows)

conn.close()