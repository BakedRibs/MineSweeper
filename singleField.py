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
        #在按钮上点击右键，触发事件
        if self.shown == False:                                                                                     #若本区域未被点开
            if self.fieldStatus == 'cover':                                                                      #若为未定状态，则变为标注旗子状态
                self.setIcon(QIcon(os.getcwd()+"/images/flag.png"))
                self.setIconSize(QSize(20, 20))
                self.fieldStatus = 'flag'                                                                          #修改为标注旗子状态
                self.rightClickSignal.emit(self.x, self.y, 10)                                                   #发送信号，将坐标和类型发送至大区域，对大区域的状态进行更新
            elif self.fieldStatus == 'flag':                                                                     #若为标注旗子状态，则变为标注问号状态
                self.setIcon(QIcon(os.getcwd()+"/images/question.png"))
                self.setIconSize(QSize(20, 20))
                self.fieldStatus = 'question'                                                                   #修改为标注问号状态
                self.rightClickSignal.emit(self.x, self.y, 11)                                                   #发送信号，将坐标和类型发送至大区域，对大区域的状态进行更新
            elif self.fieldStatus == 'question':                                                              #若为标注问号状态，则变为未定状态
                self.setIcon(QIcon(os.getcwd()+"/images/cover.png"))
                self.setIconSize(QSize(20, 20))
                self.fieldStatus = 'cover'                                                                       #修改为未定状态
                self.rightClickSignal.emit(self.x, self.y, 12)                                                  #发送信号，将坐标和类型发送至大区域，对大区域的状态进行更新
        
    def mouseReleaseEvent(self, event):
        #修改鼠标松开事件
        if event.button() == Qt.LeftButton:            #若为左键松开
            self.leftButtonClicked()                          #触发左键点击事件
        if event.button() == Qt.RightButton:          #若为右键松开
            self.rightButtonClicked()                        #触发右键点击事件
            
    def mousePressEvent(self, event):
        #修改鼠标按下事件
        if event.button() == Qt.LeftButton:           #若为左键按下
            self.showButtonPressed()                      #触发左键按下事件
                
    def showButtonSelf(self):
        #当点击空白区域时，在大区域中，需要展开并显示所有和此单元格相邻的空白区域
        #当点击雷区时，在大区域中，需要展开并显示所有雷区
        if self.shown == False:                                                                                   #若区域未点开
            if self.fieldType == 0:                                                                                #若本区域为空，且周围无雷
                self.setIcon(QIcon(os.getcwd()+"/images/blank.png"))
                self.setIconSize(QSize(20, 20))
            if 0 < self.fieldType and self.fieldType < 9:                                                   #若本区域为空，且周围有雷
                self.setIcon(QIcon(os.getcwd()+"/images/"+str(self.fieldType)+".png"))
                self.setIconSize(QSize(20, 20))
            if self.fieldType == 9:                                                                               #若本区域为雷
                self.setIcon(QIcon(os.getcwd()+"/images/whiteMine.png"))
                self.setIconSize(QSize(20, 20))
        self.shown = True                                                                                        #本区域已被展开
        
    def showButtonPressed(self):
        #当小区域被鼠标左键按下时，调用本函数
        if self.shown == False:                                                           #若区域未点开
            if self.fieldStatus == 'cover':                                             #若小区域为未定状态
                self.setIcon(QIcon(os.getcwd()+"/images/blank.png"))   #替换图片，显示小区域被按下
                self.setIconSize(QSize(20, 20))
