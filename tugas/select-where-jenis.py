import sqlite3

koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM FAUNA WHERE jenis = 'Mamalia'")
baris_table = kursor.fetchall()

print("Data Fauna:")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<20}".format("ID"," nama_fauna","jenis","asal"," jml_skrng","thn_ditemukan"))
print("--------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<10} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()