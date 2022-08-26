import pymysql

class StockDao:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def select(self, s_name):
        ret = []
        sql = f"select s_name, price from stock where s_name = '{s_name}'"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for r in rows:
            ret.append(r['price'])
        return ret
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    dao = StockDao()
  # list = dao.selects()
  # emp = dao.select('1')
  # cnt = dao.insert("홍길동", 1, "대전광역시")
  # cnt = dao.update(4, "4", 1, "4")
  # cnt = dao.delete(4)
  # print(cnt, "개의 데이터가 추가되었습니다.")