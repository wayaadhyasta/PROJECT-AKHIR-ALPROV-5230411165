import sqlite3
koneksi =sqlite3.connect("database_fauna.db")
koneksi.execute('''
    CREATE TABLE FAUNA(
    id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_fauna VARCHAR(50),
    jenis VARCHAR(50),
    asal VARCHAR(50),
    jml_skrng INTEGER(50),
    thn_ditemukan INTEGER(50)
    )
''')
koneksi.close()