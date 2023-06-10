import sqlite3

db = sqlite3.connect('inc_1.db')
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS fkko(
    title_fkko TEXT NOT NULL,
    code_fkko INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    var1 TEXT NULL,
    var2 TEXT NULL,
    var3 TEXT NULL,
    var4 TEXT NULL,
    var5 TEXT NULL,
    var6 TEXT NULL,
    var7 TEXT NULL,
    var8 TEXT NULL,
    var9 TEXT NULL,
    var10 TEXT NULL)""")


# добавление нового кода фкко
def inset_full_fkko():
    try:
        code = input('Введи код ФККО:')
        title = input('Введи название ФККО:')
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
        inset_var = """INSERT INTO fkko (title_fkko, code_fkko, 
        var1, var2, var3,  var4, var5, var6, var7, var8, var9, var10) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        data_turple = (title, code,
                       vvar1, vvar2, vvar3, vvar4, vvar5, vvar6, vvar7, vvar8, vvar9, vvar10)
        c.execute(inset_var, data_turple)
        db.commit()
        print("\nfinaly, \n")

        c.close()

    except sqlite3.Error as error:
        print("\nошибка \n", error)
    finally:
        if db:
            print("\nallright\n")


inset_full_fkko()


#поиск фкко по названию
def read_singl_str(code):
    try:
        print("\nначало чтения одиночной строки \n")
        select_one = """SELECT * FROM fkko WHERE code_fkko = ?"""

        c.execute(select_one, (code, ))

        record = c.fetchone()
        print('название ФККО', record[0])
        print('код фкко ', record[1])
        print('значение 1', record[2])
        print('значение 2', record[3])
        print('значение 3', record[4])
        print('значение 4', record[5])
        print('значение 5', record[6])
        print('значение 6', record[7])
        print('значение 7', record[8])
        print('значение 8', record[9])
        print('значение 9', record[10])
        print('значение 10', record[11])

        db.commit()
    except sqlite3.Error as e:
        print('\nошибка при чтении \n', e)
    finally:
        if db:
            db.commit()
            print('\nвсе ок \n')


#read_singl_str('2')

db.commit()
db.close()
