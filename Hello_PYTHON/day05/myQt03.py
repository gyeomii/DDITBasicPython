import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
form_class = uic.loadUiType("myQt03.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.sum)
        
    #pb가 눌리면 작동할 함수
    def sum(self) :
        txt1 = self.qle1.text()
        txt2 = self.qle2.text()
        num1 = int(txt1)
        num2 = int(txt2)
        sumNum = num1 + num2
        self.qle3.setText(str(sumNum))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()