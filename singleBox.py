import os
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class singleBox(QToolButton):
    def __init__(self, type):
        super().__init__()
        self.Init_UI(type)
        
    def Init_UI(self, type):
        self.setIcon(QIcon(os.getcwd()+"/images/cover.png"))
        self.setIconSize(QSize(20, 20))
        self.setFixedSize(QSize(20, 20))
        self.setStyleSheet("QToolButton{border-radius:0px;\
                            border:1px groove gray;}"\
                                  "QToolButton:hover{background-color:#000000;}")
