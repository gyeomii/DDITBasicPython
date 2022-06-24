import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import secrets

# UI파일 연결
form_class = uic.loadUiType("myQt06.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.createRotto)
        
    # pb가 눌리면 작동할 함수
    def createRotto(self):
        num = []
        # 리스트에 1 ~ 45 담기
        for i in range(1, 46):
            num.append(i)
        # num리스트에 담긴 데이터 중 무작위로 7개 뽑아서 rotto에 담기
        rotto = []
        for i in range(0, 7):
            rotto.append(secrets.choice(num))
            rottoSet = list(set(rotto))
        
        # 정렬하기
        rottoSet.sort()
        # 출력
        self.lbl1.setText(str(rottoSet[0]))
        self.lbl2.setText(str(rottoSet[1]))
        self.lbl3.setText(str(rottoSet[2]))
        self.lbl4.setText(str(rottoSet[3]))
        self.lbl5.setText(str(rottoSet[4]))
        self.lbl6.setText(str(rottoSet[5]))
        num.clear()
        rotto.clear()
        rottoSet.clear()

        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
