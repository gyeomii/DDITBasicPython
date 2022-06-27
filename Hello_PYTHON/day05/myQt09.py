'''
Created on 2022. 6. 24.

@author: PC 06
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
form_class = uic.loadUiType("myQt09.ui")[0]

 
# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 버튼에 기능을 연결하는 코드
        self.pbGroup = QButtonGroup()
        self.pbGroup.setExclusive(True)
        self.pbGroup.buttonClicked[int].connect(self.dial)
        self.pb_call.clicked.connect(self.call)
        
        self.pbGroup.addButton(self.pb1,1)
        self.pbGroup.addButton(self.pb2,2)
        self.pbGroup.addButton(self.pb3,3)
        self.pbGroup.addButton(self.pb4,4)
        self.pbGroup.addButton(self.pb5,5)
        self.pbGroup.addButton(self.pb6,6)
        self.pbGroup.addButton(self.pb7,7)
        self.pbGroup.addButton(self.pb8,8)
        self.pbGroup.addButton(self.pb9,9)
        self.pbGroup.addButton(self.pb0,0)
        
    # pb가 눌리면 작동할 함수
    def dial(self, id):
        for pb in self.pbGroup.buttons():
            if pb is self.pbGroup.button(id):
                txt = self.qle.text()
                txt += pb.text()
                self.qle.setText(txt)
    
    def call(self):
        QMessageBox.about(self, 'MyQt09 Calling alert', "Calling to %s"%(self.qle.text()))

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
