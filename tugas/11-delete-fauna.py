import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()


kursor.execute(f"DELETE FROM FAUNA WHERE asal = 'Kalimantan' ")
koneksi.commit()

# cek apakah data berhasil diubah atau belum
if kursor.rowcount > 0: # cek berdasarkan adanya baris atau tidak
    print(f"Data dengan ID  berhasil Dihapus!")
else:
    print(f"Tidak ada data pegawai dengan ID!")
    
koneksi.close()
    