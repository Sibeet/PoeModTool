import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from crowl import *
from functools import partial

def init_screen(ui_file):

    form_class = uic.loadUiType(ui_file)[0]
    class ModModel(QStandardItemModel):
        def __init__(self, mod_group):
            QStandardItemModel.__init__(self)

            item = QStandardItem(mod_group[0][0])
            child = QStandardItem(mod_group[0][1])
            item.appendRow(child)
            child = QStandardItem(mod_group[0][2])
            item.appendRow(child)
            self.setItem(0, 0, item)

    #화면을 띄우는데 사용되는 Class 선언
    class WindowClass(QMainWindow, form_class):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

            self.GlovesButton.clicked.connect(lambda: self.set_prefix_list('Gloves')) 
            self.GlovesButton.clicked.connect(lambda: self.set_suffix_list('Gloves'))

        def set_prefix_list(self, item_type):
            site = get_connection()
            mod_group = get_mod_group_from_tag(item_type, site)

            model = ModModel(mod_group)
            self.Prefix_List.setModel(model)

        def set_suffix_list(self, item_type):
            site = get_connection()
            mod_group = get_mod_group_from_tag(item_type, site)

            model = ModModel(mod_group)
            self.Suffix_List.setModel(model)



    app = QApplication(sys.argv) 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


init_screen('main.ui')