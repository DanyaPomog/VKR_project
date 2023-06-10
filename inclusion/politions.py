import sqlite3

db = sqlite3.connect('inc_all.db')
c = db.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS polutions(
    id INT PRIMARY KEY,
    title_car TEXT NOT NULL,
    pol_fkko INT NOT NULL,
    v1 REAL NULL,
    v2 REAL NULL,
    v3 REAL NULL,
    v4 REAL NULL,
    v5 REAL NULL,
    v6 REAL NULL,
    v7 REAL NULL,
    v8 REAL NULL,
    v9 REAL NULL,
    v10 REAL NULL)""")


#вставка нового источника загрязнения
def inset_full_polutions(car, code_p, vvar1, vvar2, vvar3, vvar4, vvar5, vvar6, vvar7, vvar8, vvar9, vvar10):
    try:
        inset_var = """INSERT INTO polutions (title_car, pol_fkko, 
        v1, v2, v3,  v4, v5, v6, v7, v8, v9, v10) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        data_turple = (car, code_p,
                       vvar1, vvar2, vvar3, vvar4, vvar5, vvar6, vvar7, vvar8, vvar9, vvar10)
        c.execute(inset_var, data_turple)
        #db.commit()
        print("\nfinaly\n")

    except sqlite3.Error as error:
        print("\nошибка\n", error)
    finally:
        if db:
            #db.close()
            print("\nallright\n")

#code_p = input('Введи код ФККО:')
#car = input('Введи название техники:')
#vvar1 = input('Введи название 1:')
#vvar2 = input('Введи название 2:')
#vvar3 = input('Введи название 3:')
#vvar4 = input('Введи название 4:')
#vvar5 = input('Введи название 5:')
#vvar6 = input('Введи название 6:')
#vvar7 = input('Введи название 7:')
#vvar8 = input('Введи название 8:')
#vvar9 = input('Введи название 9:')
#vvar10 = input('Введи название 10:')

#inset_full_polutions(car, code_p, vvar1, vvar2, vvar3, vvar4, vvar5, vvar6, vvar7, vvar8, vvar9, vvar10)


#поиск машины по названию
def read_singl_str(title_car):
    try:
        print("\nначало чтения одиночной строки\n")
        select_one = """SELECT * FROM polutions WHERE title_car = ?"""

        c.execute(select_one, (title_car, ))

        record = c.fetchone()
        print('id источника', record[0])
        print('название источника ', record[1])
        print('код фкко', record[2])
        print('значение 1', record[3])
        print('значение 2', record[4])
        print('значение 3', record[5])
        print('значение 4', record[6])
        print('значение 5', record[7])
        print('значение 6', record[8])
        print('значение 7', record[9])
        print('значение 8', record[10])
        print('значение 9', record[11])
        print('значение 10', record[12])

        db.commit()
    except sqlite3.Error as e:
        print('\nошибка при чтении\n', e)
    finally:
        if db:
            db.commit()
            print('\nвсе ок\n')


read_singl_str('2')

db.commit()
db.close()



