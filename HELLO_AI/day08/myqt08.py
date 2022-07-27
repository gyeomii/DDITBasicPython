import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import secrets
from day08.mymnist_hit_load_class import HerKY


form_class = uic.loadUiType("myqt08.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        self.le_com.clear()
        
        com = ""
        
        mine = self.le_mine.text()
        
        hky = HerKY()
        
        ans = -1
        if mine == "1":
            ans = hky.guess([[1,0,0,0,0, 0,0,0,0]])
        elif mine == "2":
            ans = hky.guess([[0,1,0,0,0, 0,0,0,0]])
        elif mine == "3":
            ans = hky.guess([[0,0,1,0,0, 0,0,0,0]])
        elif mine == "4":
            ans = hky.guess([[0,0,0,1,0, 0,0,0,0]])
        elif mine == "5":
            ans = hky.guess([[0,0,0,0,1, 0,0,0,0]])
        elif mine == "6":
            ans = hky.guess([[0,0,0,0,0, 1,0,0,0]])
        elif mine == "7":
            ans = hky.guess([[0,0,0,0,0, 0,1,0,0]])
        elif mine == "8":
            ans = hky.guess([[0,0,0,0,0, 0,0,1,0]])
        elif mine == "9":
            ans = hky.guess([[0,0,0,0,0, 0,0,0,1]])
                       
        if ans == 0:
            com = "1"
        elif ans == 1 : 
            com = "2"
        elif ans == 2 : 
            com = "3"
        elif ans == 3 : 
            com = "4"
        elif ans == 4 : 
            com = "5"
        elif ans == 5 : 
            com = "6"
        elif ans == 6 : 
            com = "7"
        elif ans == 7 : 
            com = "8"
        elif ans == 8 : 
            com = "9"
        
        self.le_com.setText(com)   
                
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()

