import sqlite3

db = sqlite3.connect('new_database.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS fkko(
    title_fkko TEXT NOT NULL,
    code_fkko INT NOT NULL PRIMARY KEY,
    var1 TEXT,
    var2 TEXT,
    var3 TEXT,
    var4 TEXT,
    var5 TEXT,
    var6 TEXT,
    var7 TEXT,
    var8 TEXT,
    var9 TEXT,
    var10 TEXT)""")

c.execute("""CREATE TABLE IF NOT EXISTS polutions(
    title_car TEXT NOT NULL,
    pol_fkko INT NOT NULL,
    v1 INT, NULL
    v2 INT,
    v3 INT,
    v4 INT,
    v5 INT,
    v6 INT,
    v7 INT,
    v8 INT,
    v9 INT,
    v10 INT)""")

db.commit()
db.close()

