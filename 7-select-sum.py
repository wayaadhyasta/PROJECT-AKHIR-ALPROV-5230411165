import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
#INSERT DATA KE TABEL

kursor.execute("SELECT SUM(jml_skrg) FROM FAUNA")#untuk mengganti jadi sum bagian avg yang diganti 
total_populasi = kursor.fetchone()[0]#ambil data gaji jaidkan baris baru

print(f"Total populasi hewan langka saat ini: {total_populasi}")#SUM UNTUK MENGHITUNG TOTAL

koneksi.close()   