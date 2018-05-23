from PyQt5.QtWidgets import QWidget, QGridLayout
from functools import partial
from singleField import singleField

class mineField(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.rowCount = 10
        self.columnCount = 12
        self.fieldMatrix = []
        for i in range(self.rowCount):
            self.fieldMatrix.append([])
            for j in range(self.columnCount):
                field = singleField(1)
                self.fieldMatrix[i].append(field)
        
        mainLayout = QGridLayout()
        for i in range(self.rowCount):
            for j in range(self.columnCount):
                mainLayout.addWidget(self.fieldMatrix[i][j], i, j)
        mainLayout.setSpacing(0)
        
        self.setLayout(mainLayout)
        
        for i in range(self.rowCount):
            for j in range(self.columnCount):
                self.fieldMatrix[i][j].clicked.connect(partial(self.singleFieldClicked, i, j))
        
    def singleFieldClicked(self, i, j):
        self.fieldMatrix[i][j].buttonClicked()
