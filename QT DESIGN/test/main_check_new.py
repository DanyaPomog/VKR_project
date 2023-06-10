from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import sys
import sqlite3
from checkNewCode import Ui_checkNewCode


db = sqlite3.connect(r"""C:\Users\pdk61\PycharmProjects\1new_maga\inclusion\hub\inc_1.db""")
c = db.cursor()


class checking(QtWidgets.QWidget):
    def __init__(self):
        super(checking, self).__init__()
        self.ui = Ui_checkNewCode()
        self.ui.setupUi(self)
        self.ui.save_new_fkko.clicked.connect(self.check_new)
        #self.ui.output_text = QtWidgets.QPlainTextEdit(self)

    def check_new(self):
        print('ass')
        l_f = self.ui.line_fkko.text()
        l_t = self.ui.line_title.text()
        db = sqlite3.connect(r"""C:\Users\pdk61\PycharmProjects\1new_maga\inclusion\hub\inc_1.db""")
        c = db.cursor()

        check_code = c.execute("""SELECT EXISTS(SELECT * FROM fkko WHERE code_fkko=?)""", (l_f,)).fetchone()
        check_title = c.execute("""SELECT EXISTS(SELECT * FROM fkko WHERE title_fkko=?)""", (l_t,)).fetchone()
        print("code = ", check_code)
        print("title = ", check_title)

        try:
            if check_code == (0,) and check_title == (0,):
                print('ok')
                print("hakuna matata")
                isert_val = """INSERT INTO fkko (code_fkko, title_fkko) VALUES (?, ?)"""
                val = (l_f, l_t)
                c.execute(isert_val, val)
                db.commit()
                c.close()
                message = str(f"Поздравляем, код ФККО {l_f} - {l_t}, успешно добавлен в базу данных")
                self.ui.output_text.setPlainText(message)
            else:
                print('else none')
                else_str = f"Такие данные уже существуют уже существует"
                self.ui.output_text.setPlainText(else_str)

        except sqlite3.Error as error:
            f = str(f"ошибка блять {error}")
            self.ui.output_text.setPlainText(f)
        finally:
            c.close()




def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = checking()
    win.show()
    sys.exit(app.exec_())


create_app()


