import sys

from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omoc02.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flagWb = False # false : 흑돌
        self.flagEnd = False
        self.pbRst.clicked.connect(self.resetGame)
        #core
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                                     ]
        
        self.pb2D = []
        
        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton('', self)
                btn.setIcon(QIcon("0.png"))
                # (10,10)을 영점으로 계속 버튼 추가
                btn.setGeometry(10+j*40,10+i*40,40,40)
                btn.setIconSize(QSize(40,40))
                btn.setToolTip("{},{}".format(i,j))
                btn.clicked.connect(self.putOmoc)
                line.append(btn)
            """ 1차원 line을 pb2D에 여러개 담아 2차원으로 만들어줌 """
            self.pb2D.append(line)
        """ "구현해주는 메소드 """    
        self.myRender()
                
    def myRender(self):
        for i in range(10):
            for j in range(10):
                if(self.arr2D[i][j] == 0):
                    self.pb2D[i][j].setIcon(QIcon("0.png"))
                if(self.arr2D[i][j] == 1):
                    self.pb2D[i][j].setIcon(QIcon("1.png"))
                if(self.arr2D[i][j] == 2):
                    self.pb2D[i][j].setIcon(QIcon("2.png"))
                
                   
    def putOmoc(self):
        if self.flagEnd:
            return
        
        pbIndex = self.sender().toolTip()
        indexArr = pbIndex.split(",")
        i = int(indexArr[0])
        j = int(indexArr[1])
        """"유효성 검사 (function의 흐름제어용)"""
        if self.arr2D[i][j] > 0:
            return
        
        storn = -1
        if self.flagWb : 
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
        
        up = self.checkUp(i, j, stone)
        dw = self.checkDW(i, j, stone)
        ri = self.checkRI(i, j, stone)
        le = self.checkLE(i, j, stone)
        ur = self.checkUR(i, j, stone)
        ul = self.checkUL(i, j, stone)
        dr = self.checkDR(i, j, stone)
        dl = self.checkDL(i, j, stone)

        d1 = up + dw + 1        
        d2 = ur + dl + 1        
        d3 = le + ri + 1        
        d4 = ul + dr + 1
        
        self.myRender()
        """승리 판별"""
        if(d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5):
            self.isVictory()
            
            
        self.flagWb = not self.flagWb
        
    """승리했을 때 팝업창"""
    def isVictory(self):
        self.flagEnd = True
        user = ""
        if self.flagWb : 
            user = "White"
        else : 
            user = "Black"
        QMessageBox.about(self, 'Victory', "%s WIN!!"%(user))
        
               
    def checkUp(self, i, j, stone):
        count = 0
        try :
            while(True):
                i -= 1
                if i < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                if j < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                
                if self.arr2D[i][j] == stone :
                    count += 1
                else:
                    return count
        except : 
            return count
            
    def checkDW(self, i, j, stone):
        count = 0
        try :
            while(True):
                i += 1
                if i < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                if j < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                
                if self.arr2D[i][j] == stone :
                    count += 1
                else:
                    return count
        except : 
            return count
        
    def checkRI(self, i, j, stone):
        count = 0
        try :
            while(True):
                j += 1
                if i < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                if j < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                
                if self.arr2D[i][j] == stone :
                    count += 1
                else:
                    return count
        except : 
            return count
        
    def checkLE(self, i, j, stone):
        count = 0
        try :
            while(True):
                j -= 1
                if i < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                if j < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                
                if self.arr2D[i][j] == stone :
                    count += 1
                else:
                    return count
        except : 
            return count
        
    def checkUR(self, i, j, stone):
        count = 0
        try :
            while(True):
                i -= 1
                j += 1
                if i < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                if j < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                
                if self.arr2D[i][j] == stone :
                    count += 1
                else:
                    return count
        except : 
            return count
        
    def checkUL(self, i, j, stone):
        count = 0
        try :
            while(True):
                i -= 1
                j -= 1
                if i < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                if j < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                
                if self.arr2D[i][j] == stone :
                    count += 1
                else:
                    return count
        except : 
            return count
        
    def checkDR(self, i, j, stone):
        count = 0
        try :
            while(True):
                i += 1
                j += 1
                if i < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                if j < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                
                if self.arr2D[i][j] == stone :
                    count += 1
                else:
                    return count
        except : 
            return count
        
    def checkDL(self, i, j, stone):
        count = 0
        try :
            while(True):
                i += 1
                j -= 1
                if i < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                if j < 0 :
                    return count # -1이 되면 배열을 뒤에서부터 읽는 에러방지용
                
                if self.arr2D[i][j] == stone :
                    count += 1
                else:
                    return count
        except : 
            return count
    """ 게임 리셋 """
    def resetGame(self):
        self.arr2D = []
        for i in range(10):
            line = []
            for j in range(10):
                line.append(0)
                
            self.arr2D.append(line)
        self.flagWb = False
        self.flagEnd = False
        self.myRender()
    
            
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()