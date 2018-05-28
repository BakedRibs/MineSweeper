import os
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, pyqtSignal

class singleField(QToolButton):
    clickSignal = pyqtSignal(int, int, int)
    def __init__(self, type, x, y):
        super().__init__()
        self.Init_UI(type, x, y)
        
    def Init_UI(self, type, x, y):
        self.fieldType = type
        self.x = x
        self.y = y
        self.leftDown = False
        self.rightDown = False
        self.bothDown = False
        self.setIcon(QIcon(os.getcwd()+"/images/cover.png"))
        self.setIconSize(QSize(20, 20))
        self.setFixedSize(QSize(20, 20))
        self.setStyleSheet("QToolButton{border-radius:0px;\
                            border:1px groove gray;}"\
                                  "QToolButton:hover{background-color:#FFFFFF;}")
                                  
    def leftButtonClicked(self):
        if self.fieldType == 9:
            self.setIcon(QIcon(os.getcwd()+"/images/whiteMine.png"))
            self.setIconSize(QSize(20, 20))
        elif self.fieldType == 0:
            self.setIcon(QIcon(os.getcwd()+"/images/blank.png"))
            self.setIconSize(QSize(20, 20))
        else:
            self.setIcon(QIcon(os.getcwd()+"/images/"+str(self.fieldType)+".png"))
            self.setIconSize(QSize(20, 20))
        self.clickSignal.emit(self.x, self.y, self.fieldType)
        
    def rightButtonClicked(self):
        pass
        
    def bothButtonClicked(self):
        pass
        
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.bothDown == True:
                if self.rightDown == False:
                    self.bothButtonClicked()
                    self.bothDown = False
            else:
                self.leftButtonClicked()
            self.leftDown = False
        if event.button() == Qt.RightButton:
            if self.bothDown == True:
                if self.leftDown == False:
                    self.bothButtonClicked()
                    self.bothDown = False
            else:
                self.rightButtonClicked()
            self.rightDown = False
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.leftDown = True
            if self.rightDown == True:
                self.bothDown = True
        if event.button() == Qt.RightButton:
            self.rightDown = True
            if self.leftDown == True:
                self.bothDown = True
