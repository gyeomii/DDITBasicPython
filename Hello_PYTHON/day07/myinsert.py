import pymysql

conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')

cur = conn.cursor() #jdbc에서 statement역할

"""
pymysql에서 %s의 역할은 단순히 데이터를 넣고자 하는 위치를 지정하는 용도
데이터의 타입과는 상관이 없다.
"""
sql = "Insert into emp values (%s, %s, %s, %s)"
val = [(3, "3", "3", "3"), (4, "4", "4", "4")]

cur.executemany(sql, val)



conn.commit()
print(cur.rowcount, "개의 레코드가 입력되었습니다.")

cur.close()
conn.close()