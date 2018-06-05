import os
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, pyqtSignal

class singleField(QToolButton):
    #单独的一个小区域，继承了QToolButton的属性
    #小区域可能为空且周围不包含雷，可能为空且周围包含雷，可能为雷
    leftClickSignal = pyqtSignal(int, int, int)           #点击鼠标左键，发出信号
    rightClickSignal = pyqtSignal(int, int, int)         #点击鼠标右键，发出信号
    def __init__(self, type, x, y):
        #初始化函数，xy为在区域中的横纵坐标，type为小区域类型
        super().__init__()
        self.Init_UI(type, x, y)
        
    def Init_UI(self, type, x, y):
        self.shown = False                                                            #本区域是否已经显示，初始化为否
        self.fieldType = type                                                         #本区域类型，0为空，1-8为周围雷数，9为雷
        self.fieldStatus = 'cover'                                                 #本区域状态，包含未点开、标注旗子和标注问号几种状态
        self.x = x                                                                        #在大区域中横坐标
        self.y = y                                                                       #在大区域中纵坐标
        self.setIcon(QIcon(os.getcwd()+"/images/cover.png"))
        self.setIconSize(QSize(20, 20))
        self.setFixedSize(QSize(20, 20))
        self.setStyleSheet("QToolButton{border-radius:0px;\
                            border:1px groove gray;}"\
                                  "QToolButton:hover{background-color:#FFFFFF;}")
                                  
    def leftButtonClicked(self):
        #在按钮上点击左键，触发事件
        if self.shown == False:                                                                                      #若本区域未被点开
            if self.fieldStatus == 'cover':                                                                       #若为未定状态，而非标注旗子状态，则可以点开
                if self.fieldType == 9:                                                                               #若为雷
                    self.setIcon(QIcon(os.getcwd()+"/images/redMine.png"))                       #被点开的雷标注为红色，其他雷标注为白色，以进行区分
                    self.setIconSize(QSize(20, 20))
                elif self.fieldType == 0:                                                                            #若为空
                    self.setIcon(QIcon(os.getcwd()+"/images/blank.png"))                          #背景图片修改为空
                    self.setIconSize(QSize(20, 20))
                else:
                    self.setIcon(QIcon(os.getcwd()+"/images/"+str(self.fieldType)+".png"))  #本区域不为雷，但周围包含1-8个雷，修改为特定数字
                    self.setIconSize(QSize(20, 20))
                self.shown = True                                                                                    #不论为何状态，均标注为点开
                self.leftClickSignal.emit(self.x, self.y, self.fieldType)                                       #发送信号，将坐标和类型发送至大区域，由大区域继续进行处理
        
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
