import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from dask.array.random import randint

#UI파일 연결
form_class = uic.loadUiType("myQt05.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.oddEven)
        self.qle1.returnPressed.connect(self.oddEven)
        
    #pb가 눌리면 작동할 함수
    def oddEven(self) :
        User = self.qle1.text()
        com = self.comRand()
        if(User == com):
            result = "User 승리"
        else:
            result = "Com 승리"
        self.qle2.setText(com)
        self.qle3.setText(result)
        
    def comRand(self):
        com = ""
        rnd = randint(0,2)
        if(rnd == 0):
            com = "짝"
        else:
            com = "홀"
        return com
               
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()