import sqlite3

db1 = sqlite3.connect('inc_all.db')
c1 = db1.cursor()

#отходы минеральных масел трансмиссионных
def r_40615001313():
    try:
        print('1')
        find_code = input('введи код фкко')

        select_row_pol = """SELECT * FROM polutions WHERE pol_fkko = ?"""
        print('2')

        c1.execute(select_row_pol, (find_code,))
        print('3')
        rows = c1.fetchall()
        print(rows)

        for i in rows:
            print(i)
            output = (i[3] * i[4] * i[5] * i[6] * i[7] * i[10] * i[9]) / i[8] * 0.001
            print(round(output, 3))

    except sqlite3.Error as e:
        print('ошибка при чтении \n', e)
    finally:
        if db1:
            db1.commit()
            print('все ок \n')

r_40615001313()

#фильтры очистки топлива автотранспортных средств отработанные
def r_92130301523():
    try:
        print('1')
        find_code = input('введи код фкко')

        select_row_pol = """SELECT * FROM polutions WHERE pol_fkko = ?"""
        print('2')

        c1.execute(select_row_pol, (find_code,))
        print('3')
        rows = c1.fetchall()
        print(rows)

        for i in rows:
            print(i)
            output = i[3] * i[4] * i[5] * i[6] / i[7] / 1000000
            print(round(output, 3))

    except sqlite3.Error as e:
        print('ошибка при чтении \n', e)
    finally:
        if db1:
            db1.commit()
            print('все ок \n')


#r_92130301523()

db1.commit()
db1.close()

# 40615001313