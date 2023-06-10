from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from tableW import Ui_MainWindow
import sys
import sqlite3
from checkNewCode import Ui_checkNewCode

db = sqlite3.connect(r"""C:\Users\pdk61\PycharmProjects\1new_maga\inclusion\hub\inc_1.db""")
c = db.cursor()



class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadValues()
        self.ui.create_button.clicked.connect(self.openCheck)
        self.ui.exit_but.clicked.connect(self.close_window)

    def loadValues(self):
        row_count = ("""SELECT COUNT(*) FROM fkko""")
        c.execute(row_count)
        r = c.fetchone()
        rec = r[0]
        #column_count = ("""SELECT COUNT(*) FROM fkko""")
        self.ui.tableWidget.setRowCount(rec)
        self.ui.tableWidget.setColumnCount(14)

        self.ui.tableWidget.setHorizontalHeaderLabels(('КОД ФККО', "ЭНАЗВАНИЕ ФККО", "НАЗВАНИЕ МАШИНЫ"))

        join_table = """SELECT title_fkko, code_fkko, title_car FROM fkko, polutions
            WHERE polutions.pol_fkko = fkko.code_fkko
            """
        c.execute(join_table)
        table = c.fetchall()

        row_index = 0
        for t in table:
            self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(t[1])))
            self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(t[0])))
            self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(t[2])))
            row_index += 1

        var_table = """SELECT v1, v2, v3, v4, v5, v6, v7, v8, v9 FROM fkko, polutions
            WHERE polutions.pol_fkko = fkko.code_fkko 
            """
        c.execute(var_table)
        var = c.fetchall()

        row_index = 0
        for v in var:
            self.ui.tableWidget.setItem(row_index, 3, QTableWidgetItem(str(v[0])))
            self.ui.tableWidget.setItem(row_index, 4, QTableWidgetItem(str(v[1])))
            self.ui.tableWidget.setItem(row_index, 5, QTableWidgetItem(str(v[2])))
            self.ui.tableWidget.setItem(row_index, 6, QTableWidgetItem(str(v[3])))
            self.ui.tableWidget.setItem(row_index, 7, QTableWidgetItem(str(v[4])))
            self.ui.tableWidget.setItem(row_index, 8, QTableWidgetItem(str(v[5])))
            self.ui.tableWidget.setItem(row_index, 9, QTableWidgetItem(str(v[6])))
            self.ui.tableWidget.setItem(row_index, 10, QTableWidgetItem(str(v[7])))
            self.ui.tableWidget.setItem(row_index, 11, QTableWidgetItem(str(v[8])))
            row_index += 1

    def openCheck(self):
        #global checking
        checking = QtWidgets.QDialog(self)
        ui = Ui_checkNewCode()
        ui.setupUi(checking)
        checking.show()

    def close_window(self):
        result = QMessageBox.question(self, "Закрыть", "Вы уверены, что хотите закрыть приложение?",
                                      QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore,
                                      QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            QtWidgets.qApp.quit()
        else:
            print('continea')


def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())


create_app()


