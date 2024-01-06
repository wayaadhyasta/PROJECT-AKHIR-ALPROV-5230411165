import sqlite3

koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM FAUNA WHERE jml_skrg <= '1000'")
baris_tabel = kursor.fetchall()

#Membuat format tabel dengan method format()
print("Data Fauna")
print("="*126)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID Fauna", "Nama Fauna", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Terakhir Ditemukan"))
print("-"*126)
#Tampilkan data sesuai format tabel dg perulangan
for baris in baris_tabel:
    print("{:<10} {:<19} {:<20} {:<25} {:<22} {:<22}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()