import random
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import pyqtSignal
from singleField import singleField

class mineField(QWidget):
    clickMine = pyqtSignal()                                                                                 #触雷事件
    finishClean = pyqtSignal()                                                                               #区域全部清空事件
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        #对界面和参数进行初始化
        self.rowCount = 16                                                                                    #行数
        self.columnCount = 20                                                                               #列数
        self.mineCount = 10                                                                                  #总雷数
        self.remainMineCount = self.mineCount                                                         #剩余雷数
        self.clear = 0                                                                                           #已探出的非雷区域
        self.clearGoal = self.rowCount * self.columnCount - self.mineCount                   #剩余未探出的非雷区域
        
        self.matrixInitiate()                                                                                   #对雷区、周围数字和按钮等进行初始化
        
        mainLayout = QGridLayout()
        for i in range(self.rowCount):
            for j in range(self.columnCount):
                mainLayout.addWidget(self.fieldMatrix[i][j], i, j)                                     #QGridLayout布局
        mainLayout.setSpacing(0)
        
        self.setLayout(mainLayout)
        
        for i in range(self.rowCount):
            for j in range(self.columnCount):
                self.fieldMatrix[i][j].leftClickSignal.connect(self.leftButtonClicked)             #左键点击处理函数
                self.fieldMatrix[i][j].rightClickSignal.connect(self.rightButtonClicked)          #右键点击处理函数
        
    def leftButtonClicked(self, x, y, type):
        #左键点击处理函数
        if type == 9:                                                                                          #左键点击雷区
            self.shown[x][y] = 1
            for i in range(self.rowCount):
                for j in range(self.columnCount):
                    if self.numberMatrix[i][j] == 9:
                        if self.shown[i][j] == 0:                                                            #若此区域未被显示
                            self.fieldMatrix[i][j].showButtonSelf()                                      #显示此区域（中的雷）
                            self.shown[i][j] = 1                                                             #此区域已被显示
            self.clickMine.emit()                                                                            #发出触雷事件
        elif type == 0:                                                                                      #左键点击空白区
            if self.shown[x][y] == 0:                                                                     #若此区域未被显示
                blankMap = []
                self.shown[x][y] = 1
                self.clear += 1
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
                                            self.clear += 1
                if self.clear == self.clearGoal:
                    self.finishClean.emit()
        else:
            self.shown[x][y] = 1
            self.clear += 1
            if self.clear == self.clearGoal:
                self.finishClean.emit()
        
    def rightButtonClicked(self, x, y, type):
        if type == 10 or type == 11:
            if self.numberMatrix[x][y] == 9:
                self.remainMineCount -= 1
        elif type == 12:
            if self.numberMatrix[x][y] == 9:
                self.remainMineCount += 1
        
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
        while len(self.minePos) < self.mineCount:
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
