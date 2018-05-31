import os
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, pyqtSignal

class singleField(QToolButton):
    leftClickSignal = pyqtSignal(int, int, int)
    rightClickSignal = pyqtSignal(int, int, int)
    def __init__(self, type, x, y):
        super().__init__()
        self.Init_UI(type, x, y)
        
    def Init_UI(self, type, x, y):
        self.shown = False
        self.fieldType = type
        self.fieldStatus = 'cover'
        self.x = x
        self.y = y
        self.setIcon(QIcon(os.getcwd()+"/images/cover.png"))
        self.setIconSize(QSize(20, 20))
        self.setFixedSize(QSize(20, 20))
        self.setStyleSheet("QToolButton{border-radius:0px;\
                            border:1px groove gray;}"\
                                  "QToolButton:hover{background-color:#FFFFFF;}")
                                  
    def leftButtonClicked(self):
        if self.shown == False:
            if self.fieldStatus == 'cover':
                if self.fieldType == 9:
                    self.setIcon(QIcon(os.getcwd()+"/images/redMine.png"))
                    self.setIconSize(QSize(20, 20))
                elif self.fieldType == 0:
                    self.setIcon(QIcon(os.getcwd()+"/images/blank.png"))
                    self.setIconSize(QSize(20, 20))
                else:
                    self.setIcon(QIcon(os.getcwd()+"/images/"+str(self.fieldType)+".png"))
                    self.setIconSize(QSize(20, 20))
                self.shown = True
                self.leftClickSignal.emit(self.x, self.y, self.fieldType)
        
    def rightButtonClicked(self):
        if self.shown == False:
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
            elif self.fieldStatus == 'question':
                self.setIcon(QIcon(os.getcwd()+"/images/cover.png"))
                self.setIconSize(QSize(20, 20))
                self.fieldStatus = 'cover'
                self.rightClickSignal.emit(self.x, self.y, 12)
        
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.leftButtonClicked()
        if event.button() == Qt.RightButton:
            self.rightButtonClicked()
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.showButtonPressed()
                
    def showButtonSelf(self):
        if self.shown == False:
            if self.fieldType == 0:
                self.setIcon(QIcon(os.getcwd()+"/images/blank.png"))
                self.setIconSize(QSize(20, 20))
            if 0 < self.fieldType and self.fieldType < 9:
                self.setIcon(QIcon(os.getcwd()+"/images/"+str(self.fieldType)+".png"))
                self.setIconSize(QSize(20, 20))
            if self.fieldType == 9:
                self.setIcon(QIcon(os.getcwd()+"/images/whiteMine.png"))
                self.setIconSize(QSize(20, 20))
        self.shown = True
        
    def showButtonPressed(self):
        if self.shown == False:
            if self.fieldStatus == 'cover':
                self.setIcon(QIcon(os.getcwd()+"/images/blank.png"))
                self.setIconSize(QSize(20, 20))
