from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from table import Ui_MainWindow
import sys

import sqlite3

db = sqlite3.connect(r"""C:\Users\pdk61\PycharmProjects\1new_maga\inclusion\hub\inc_1.db""")
c = db.cursor()


class Window(QtWidgets.QMainWindow):
    def __int__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProduct()

    def loadProduct(self):
        row_count = """"SELECT COUNT(*) FROM fkko.code_fkko"""
        print(row_count)
        self.ui.tableView.setRowCount(3)
        self.ui.tableView.setColumnCount(4)


def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())



create_app()