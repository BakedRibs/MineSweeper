import os
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, pyqtSignal

class singleField(QToolButton):
    leftClickSignal = pyqtSignal(int, int, int)
    rightClickSignal = pyqtSignal(int, int, int)
    bothClickSignal = pyqtSignal(int, int, int)
    def __init__(self, type, x, y):
        super().__init__()
        self.Init_UI(type, x, y)
        
    def Init_UI(self, type, x, y):
        self.fieldType = type
        self.fieldStatus = 'cover'
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
        self.leftClickSignal.emit(self.x, self.y, self.fieldType)
        
    def rightButtonClicked(self):
        if self.fieldStatus == 'cover':
            self.setIcon(QIcon(os.getcwd()+"/images/flag.png"))
            self.setIconSize(QSize(20, 20))
            self.fieldStatus = 'flag'
            self.rightClickSignal.emit(self.x, self.y, 10)
        elif self.fieldStatus == 'flag':
            self.setIcon(QIcon(os.getcwd()+"/images/question.png"))
            self.setIconSize(QSize(20, 20))
            self.fieldStatus = 'question'
            self.rightClickSignal.emit(self.x, self.y, 11)
        else:
            self.setIcon(QIcon(os.getcwd()+"/images/cover.png"))
            self.setIconSize(QSize(20, 20))
            self.fieldStatus = 'cover'
            self.rightClickSignal.emit(self.x, self.y, 12)
        
    def bothButtonClicked(self):
        self.bothClickSignal.emit(self.x, self.y, 99)
        
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
