import pymysql

class StockSyncDao:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='_stock_old', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectPrice(self,s_code):
        ret=[]
        sql = f"select {s_code} from stock_sync_0121"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for r in rows:
            ret.append(r[s_code])
        return ret
    
    def selectCode(self):
        ret=[]
        sql = f""" SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = 'stock_sync_0121' """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for r in rows:
            ret.append(r['COLUMN_NAME'])
        ret.remove('in_time')
        return ret
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    # dao = StockSyncDao()
    # list = dao.selectCode()
    # print(list)