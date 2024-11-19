import sqlite3
con = sqlite3.connect("DB1.db")
cur = con.cursor()
a = input('masukkan nomor: ')
b = input('masukkan nama: ')
cur.execute("""
    insert into TBL1 values
            ({},'{}')
""".format(a,b))
con.commit()