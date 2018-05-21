from PyQt5.QtWidgets import QWidget, QGridLayout
from singleBox import singleBox

class mineZone(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        single = singleBox()
        
        mainLayout = QGridLayout()
        mainLayout.addWidget(single, 0, 0)
        
        self.setLayout(mainLayout)
