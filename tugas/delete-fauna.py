import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Menjalankan query DELETE
asal = "kalimantan"  # ID pegawai yang akan dihapus
cursor.execute(f"DELETE FROM FAUNA WHERE asal = ?", (asal,))
conn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if cursor.rowcount > 0:
    print(f"Data pegawai dengan ID {asal} berhasil dihapus.")
else:
    print(f"Tidak ada data pegawai dengan ID {asal}.")

# Menutup koneksi
conn.close()
