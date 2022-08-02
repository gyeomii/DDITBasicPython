import pymysql

class DaoGibo:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def getPanMax(self):
        mymax=0
        sql = f"""
            Select IFNULL(max(pan),0)+1 as max from gibo
            """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        mymax = rows[0]['max']
        return mymax
        
    def insert(self, pan, win, gibos, gibos_ai, anss):
        cnt = 0
        
        for i in range(len(anss)):
            gibo = gibos[i]
            gibo_ai = gibos_ai[i]
            ans = anss[i]
            sql = f"""
                Insert into gibo (pan, win, gibo, gibo_ai, ans) 
                values ('{pan}', '{win}', '{gibo}', '{gibo_ai}', '{ans}')
            """
            # 문자열 입력할 때 앞뒤로 ' ' 중요
            cnt += self.cur.execute(sql)
        self.conn.commit()
        return cnt    

    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    pan = "1"
    win = "2"
    gibo = ["1","1"]
    gibo_ai = ["x","x"]
    ans = ["0","1"]
    dao = DaoGibo()
    # mymax = dao.getPanMax()
    # print("max",mymax)