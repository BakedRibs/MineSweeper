import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
from mineField import mineField

class MineSweeper(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.field = mineField()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.field)
        
        self.setLayout(mainLayout)
        
        self.field.clickMine.connect(self.mineClicked)
        self.field.finishClean.connect(self.cleaningFinished)
        
        self.show()
        
    def mineClicked(self):
        pass
        
    def cleaningFinished(self):
        pass
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MS = MineSweeper()
    app.exit(app.exec_())
