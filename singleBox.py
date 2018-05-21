import os
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class singleBox(QToolButton):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.setIcon(QIcon(os.getcwd()+"/images/cover.png"))
        self.setIconSize(QSize(30, 30))
