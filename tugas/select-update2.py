# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Data yang ingin diubah
id_fauna = 4
asal = 'Kalimantan Timur'

# Menjalankan query UPDATE
cursor.execute(f"UPDATE FAUNA SET asal = {asal} WHERE id_fauna = {id_fauna}")
conn.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data pegawai dengan ID {id_fauna} berhasil diupdate.")
else:
    print(f"Tidak ada data pegawai dengan ID {id_fauna}.")

# Menutup koneksi
conn.close()
