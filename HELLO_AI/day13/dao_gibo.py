import pymysql
import numpy as np

class DaoGibo:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectGiboAi(self):
        gibos_ai = []
        anss = []
        
        gibos_ai_pp = []
        
        sql = f"""
            Select gibo_ai, ans from gibo
            """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            gibos_ai.append(row['gibo_ai'])
            anss.append(row['ans'])
            
        for h4 in gibos_ai:
            line = []
            for i in range(400):
                hanjari = h4[i:i+1]
                if hanjari == "0":
                    line.append(0)
                if hanjari == "1":
                    line.append(1)
                if hanjari == "x":
                    line.append(-1)
            gibos_ai_pp.append(line)
            
        # line_trash = []
        # for i in range(400):
        #     line_trash.append(-1)        
        # gibos_ai_pp.append(line_trash)
        # anss.append(399)
        
        gibos_ai_pp_n = np.array(gibos_ai_pp)
        anss_n = np.array(anss)
            
        print(gibos_ai_pp_n)
        print(anss_n)
        np.save("omok_train2", gibos_ai_pp_n)
        np.save("omok_answer2", anss_n)
        
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
    dao.selectGiboAi()
    # mymax = dao.getPanMax()
    # print("max",mymax)