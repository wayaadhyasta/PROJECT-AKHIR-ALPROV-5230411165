import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

# Menjalankan query SELECT dengan ORDER BY
kursor.execute("SELECT * FROM FAUNA ORDER BY nama_fauna ASC") #ASC|DESC
baris_table = kursor.fetchall()

print("Data Fauna:")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<10}".format("ID", "Nama", "Jenis", "Asal", "Jumlah Sekarang","Tahun Terakhir Ditemukan"))
print("--------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4]))
    
koneksi.close()