import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Menjalankan query DELETE
asal = "Kalimantan"  # Ganti dengan kriteria yang sesuai untuk data yang ingin dihapus
cursor.execute("DELETE FROM FAUNA WHERE asal = ?", (asal,))
conn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if cursor.rowcount > 0:
    print(f"Data fauna dengan Asal {asal} berhasil dihapus.")
else:
    print(f"Tidak ada data fauna dengan Asal {asal}.")

# Menutup koneksi
conn.close()
