'''
Created on 2022. 6. 24.

@author: PC 06
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import secrets

# UI파일 연결
form_class = uic.loadUiType("myQt07.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.rsp)
        self.qle1.returnPressed.connect(self.rsp)
        
    #pb가 눌리면 작동할 함수
    def rsp(self) :
        user = self.qle1.text()
        comList = ["가위", "바위", "보"]
        com = secrets.choice(comList)
        if(user == com):
            result = "비김"
        elif(user == "가위" and com == "보" 
             or user == "바위" and com == "가위" 
             or user == "보" and com == "바위"):
            result = "User 승리"
        else:
            result = "COM 승리"
        self.qle2.setText(com)
        self.qle3.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()