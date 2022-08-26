import sys

from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omoc01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flagWb = True;
        
        for j in range(19):
            for i in range(19):
                btn = QPushButton('', self)
                btn.setIcon(QIcon("0.png"))
                btn.setGeometry(10+i*40,10+j*40,40,40)
                btn.setIconSize(QSize(40,40))
                btn.clicked.connect(self.putOmoc)
                
                
    def putOmoc(self):
        if self.flagWb :
            self.sender().setIcon(QIcon("1.png"))
        else :    
            self.sender().setIcon(QIcon("2.png"))
        self.flagWb = not self.flagWb
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()