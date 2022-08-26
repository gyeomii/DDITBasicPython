import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
form_class = uic.loadUiType("myQt04.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.gugudan)
        
    #pb가 눌리면 작동할 함수
    def gugudan(self) :
        txt = self.qle.text()
        num = int(txt)
        form = ""
        for i in range(1,10):
            form += "%d * %d  = %d\n" %(num, i, num*i)
            
        self.pte.setPlainText(form)
           
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()