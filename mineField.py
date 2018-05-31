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
                self.fieldMatrix[i][j].leftClickSignal.connect(self.leftButtonClicked)
                self.fieldMatrix[i][j].rightClickSignal.connect(self.rightButtonClicked)
                self.fieldMatrix[i][j].bothClickSignal.connect(self.bothButtonClicked)
        
    def leftButtonClicked(self, x, y, type):
        if type == 9:
            self.shown[x][y] = 1
            for i in range(self.rowCount):
                for j in range(self.columnCount):
                    if self.numberMatrix[i][j] == 9:
                        if self.shown[i][j] == 0:
                            self.fieldMatrix[i][j].showButtonSelf()
                            self.shown[i][j] = 1
        elif type == 0:
            if self.shown[x][y] == 0:
                blankMap = []
                self.shown[x][y] = 1
                for i in range(self.rowCount):
                    blankMap.append([])
                    for j in range(self.columnCount):
                        blankMap[i].append(0)
                blankMap[x][y] = 1
                self.findAllConnectedBlank(x, y, blankMap)
                for i in range(self.rowCount):
                    for j in range(self.columnCount):
                        if blankMap[i][j] == 1:
                            for p in [-1, 0, 1]:
                                for q in [-1, 0, 1]:
                                    if 0 <= i+p and i+p < self.rowCount and 0 <= j+q and j+q < self.columnCount:
                                        if self.shown[i+p][j+q] == 0:
                                            self.fieldMatrix[i+p][j+q].showButtonSelf()
                                            self.shown[i+p][j+q] = 1
        else:
            self.shown[x][y] = 1
        
    def rightButtonClicked(self, x, y, type):
        pass
        
    def bothButtonClicked(self, x, y, type):
        pass
        
    def findAllConnectedBlank(self, x, y, blankMap):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= x+i and x+i < self.rowCount and 0 <= y+j and y+j < self.columnCount:
                    if blankMap[x+i][y+j] == 0:
                        if self.numberMatrix[x+i][y+j] == 0:
                            blankMap[x+i][y+j] = 1
                            self.findAllConnectedBlank(x+i, y+j, blankMap)
        
    def matrixInitiate(self):
        self.numberMatrix = []
        self.shown = []
        for i in range(self.rowCount):
            self.numberMatrix.append([])
            self.shown.append([])
            for j in range(self.columnCount):
                self.numberMatrix[i].append(0)
                self.shown[i].append(0)
                
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
