import pymysql

class EmpDao:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selects(self):
        sql = "select * from emp"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows
    
    def select(self, e_id):
        sql = f"""
            select e_id, e_name, sex, addr 
            from emp 
            where e_id={e_id}
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows[0]
        
    def insert(self, e_name, sex, addr):
        sql = f"""
            Insert into emp (e_name, sex, addr) 
            values ('{e_name}', {sex}, '{addr}')
        """
        # 문자열 입력할 때 앞뒤로 ' ' 중요
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, e_id, e_name, sex, addr):
        sql = f"""
             Update emp 
             set e_name='{e_name}', sex='{sex}', addr='{addr}' 
             where e_id = {e_id}
        """
        cnt= self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, e_id):
        sql = f"""
            delete from emp 
            where e_id='{e_id}'
        """
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    

    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    dao = EmpDao()
  # list = dao.selects()
  # emp = dao.select('1')
  # cnt = dao.insert("홍길동", 1, "대전광역시")
  # cnt = dao.update(4, "4", 1, "4")
  # cnt = dao.delete(4)
  # print(cnt, "개의 데이터가 추가되었습니다.")