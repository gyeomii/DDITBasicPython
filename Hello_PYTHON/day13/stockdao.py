import pymysql

class StockDao:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
        
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def insert(self, s_code, ymd, s_name, price):
        sql = f"""
            Insert into stock (s_code, ymd, s_name, price) 
            values ('{s_code}', '{ymd}', '{s_name}', '{price}')
        """
        # 문자열 입력할 때 앞뒤로 ' ' 중요
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt

    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    dao = StockDao()