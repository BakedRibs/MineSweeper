import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QApplication, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from mineField import mineField

class MineSweeper(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.initButton = QToolButton()
        self.initButton.setIcon(QIcon(os.getcwd()+"/images/smile.png"))
        self.initButton.setIconSize(QSize(32, 32))
        
        controlBar = QHBoxLayout()
        controlBar.addStretch()
        controlBar.addWidget(self.initButton)
        controlBar.addStretch()
        
        self.field = mineField()
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(controlBar)
        self.mainLayout.addWidget(self.field)
        
        self.setLayout(self.mainLayout)
        
        self.field.clickMine.connect(self.mineClicked)
        self.field.finishClean.connect(self.cleaningFinished)
        self.initButton.clicked.connect(self.newField)
        
        self.show()
        
    def mineClicked(self):
        self.field.setEnabled(False)
        self.initButton.setIcon(QIcon(os.getcwd()+"/images/cry.png"))
        self.initButton.setIconSize(QSize(32, 32))
        
    def cleaningFinished(self):
        self.field.setEnabled(False)
        self.initButton.setIcon(QIcon(os.getcwd()+"/images/smile.png"))
        self.initButton.setIconSize(QSize(32, 32))
        
    def newField(self):
        self.mainLayout.removeWidget(self.field)
        self.field = mineField()
        self.mainLayout.addWidget(self.field)
        self.setLayout(self.mainLayout)
        self.initButton.setIcon(QIcon(os.getcwd()+"/images/smile.png"))
        self.initButton.setIconSize(QSize(32, 32))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MS = MineSweeper()
    app.exit(app.exec_())
