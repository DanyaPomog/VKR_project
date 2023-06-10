param = ''
print(type(param))

vvar1 = input('Введи название 1:')
vvar2 = input('Введи название 2:')
vvar3 = input('Введи название 3:')
vvar4 = input('Введи название 4:')
vvar5 = input('Введи название 5:')
vvar6 = input('Введи название 6:')
vvar7 = input('Введи название 7:')
vvar8 = input('Введи название 8:')
vvar9 = input('Введи название 9:')
vvar10 = input('Введи название 10:')

while count != len_:
    count += 1
    if count != len_:
        print(count)
        ins = input('введите название параметра')
        param = list(param)
        param.append(ins)
        param = tuple(param)
        print(param)
    elif count == len_:
        print('end circle')
        return param




        select_code = """SELECT code_fkko FROM fkko"""
        c.execute(select_code)
        code = c.fetchall()
        print(code)

        select_title = """SELECT title_fkko FROM fkko"""
        c.execute(select_title)
        title = c.fetchall()
        print(title)

        select_car = """SELECT title_car FROM polutions"""
        c.execute(select_car)
        car = c.fetchall()
        print(car)

        row_index = 0
        for piss in titleAcode:
            self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(piss[0])))
            self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(piss[1])))

            for cr in car:
                print(cr)
                for ca in cr:
                    self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(ca)))
            row_index += 1


    def data_save(self):
        c_fkko = self.ui.line_code.text()
        t_fkko = self.ui.line_title.text()

        if c_fkko and t_fkko is not None:
            rowCount = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowCount)
            self.ui.tableWidget.setItem(rowCount, 0, QTableWidgetItem(c_fkko))
            self.ui.tableWidget.setItem(rowCount, 1, QTableWidgetItem(t_fkko))





 def check_new(self):
        print('ass')
        l_f = self.ui.line_fkko.text()
        l_t = self.ui.line_title.text()

        if l_t or l_f is not None:
            db = sqlite3.connect(r"""C:\Users\pdk61\PycharmProjects\1new_maga\inclusion\hub\inc_1.db""")
            c = db.cursor()

            check = """SELECT code_fkko FROM fkko"""
            c.execute(check)
            res = c.fetchall()
            print(res)
            print(l_t, l_f)
            try:
                #for r in res:
                   # print(r)
                if l_f or l_t not in res:
                    print("hakuna matata")
                    isert_val = """INSERT INTO fkko (code_fkko, title_fkko) VALUES (?, ?)"""
                    val = (l_f, l_t)
                    c.execute(isert_val, val)
                    db.commit()
                    c.close()

                    self.ui.output_label.setText(str(f"Поздравляем, код ФККО {l_f} - {l_t}, успешно добавлен в базу данных"), self,)
                else:
                    self.ui.output_label.setText(str(f"Данный код ФККО уже существует"))
            except sqlite3.Error as error:
                f =("ошибка блять", error)
                self.ui.setText(str(f))
            finally:

                if db:
                    c.close()

                db.close()
