import pymysql

conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')

cur = conn.cursor() #jdbc에서 statement역할

# python 3.5 이상부터는 fString을 쓸 수 있다.

e_id = "3"

sql = f"""
delete from
    emp 
where
    e_id='{e_id}'
"""

cnt= cur.execute(sql)

conn.commit()
print(cnt, "개의 레코드가 삭제되었습니다.")

cur.close()
conn.close()