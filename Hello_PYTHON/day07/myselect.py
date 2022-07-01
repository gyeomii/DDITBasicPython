import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python',
                        db='python', charset='utf8')

cur = conn.cursor() #jdbc에서 statement역할

sql = "select * from emp"
cur.execute(sql)

rows = cur.fetchall() #튜플데이터로 출력 (멀티리턴)
print(rows)

cur.close()
conn.close()