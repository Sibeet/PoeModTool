import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from crowl import *

def init_screen(ui_file):
    #UI파일 연결
    #단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
    form_class = uic.loadUiType(ui_file)[0]


    #화면을 띄우는데 사용되는 Class 선언
    class WindowClass(QMainWindow, form_class) :
        site = get_connection()
        armour_list = get_armour_list('gloves', site)
        tag_modifier = get_tag_modifier('gloves', site)
        def __init__(self) :
            super().__init__()
            self.setupUi(self)

            self.GlovesButton.clicked.connect(self.set_ModGroupList)


        def set_ModGroupList(self):
            data = ['a', 'b', 'c', 'd']
            model = QStandardItemModel()
            for val in data:
                model.appendRow(QStandardItem(val))

            self.ModGroupList.setModel(model)


    app = QApplication(sys.argv) 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


init_screen('main.ui')