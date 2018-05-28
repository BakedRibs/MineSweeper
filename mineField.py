import random
from PyQt5.QtWidgets import QWidget, QGridLayout
from singleField import singleField

class mineField(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.rowCount = 16
        self.columnCount = 20
        self.mineCount = 20
        
        self.matrixInitiate()
        
        mainLayout = QGridLayout()
        for i in range(self.rowCount):
            for j in range(self.columnCount):
                mainLayout.addWidget(self.fieldMatrix[i][j], i, j)
        mainLayout.setSpacing(0)
        
        self.setLayout(mainLayout)
        
        for i in range(self.rowCount):
            for j in range(self.columnCount):
                self.fieldMatrix[i][j].clickSignal.connect(self.leftButtonClicked)
        
    def leftButtonClicked(self, x, y, type):
        pass
        
    def matrixInitiate(self):
        self.numberMatrix = []
        for i in range(self.rowCount):
            self.numberMatrix.append([])
            for j in range(self.columnCount):
                self.numberMatrix[i].append(0)
                
        self.minePos = []
        while len(self.minePos) < 20:
            newMine = (random.randint(0, self.rowCount-1), random.randint(0, self.columnCount-1))
            if newMine not in self.minePos:
                self.minePos.append(newMine)
                
        for mine in self.minePos:
            self.numberMatrix[mine[0]][mine[1]] = 9
            
        for i in range(self.rowCount):
            for j in range(self.columnCount):
                if self.numberMatrix[i][j] != 9:
                    count = 0
                    for p in (-1, 0, 1):
                        for q in (-1, 0, 1):
                            if i+p >= 0 and i+p < self.rowCount and j+q >= 0 and j+q < self.columnCount:
                                if self.numberMatrix[i+p][j+q] == 9:
                                    count += 1
                    self.numberMatrix[i][j] = count
        
        self.fieldMatrix = []
        for i in range(self.rowCount):
            self.fieldMatrix.append([])
            for j in range(self.columnCount):
                field = singleField(self.numberMatrix[i][j], i, j)
                self.fieldMatrix[i].append(field)
