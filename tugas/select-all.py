import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()
kursor.execute("SELECT *FROM FAUNA")
baris_tabel = kursor.fetchall()

print("Data Pegawai Konoha 2023")
print("="*80)
print("{:<5}{:<20}{:<20}{:<20}{:<20}".format("ID"," nama_fauna","jenis","asal"," jml_skrng","thn_ditemukan"))
print("="*80)

for baris in baris_tabel:
    print("{:<5}{:<20}{:<20}{:<20}{:<20}".format (baris[0],baris[1],baris[2],baris[3],baris[4]))
koneksi.close()