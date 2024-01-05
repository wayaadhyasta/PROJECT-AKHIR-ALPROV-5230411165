import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()



kursor.execute("""UPDATE FAUNA SET asal = 'Kalimantan Timur'  WHERE id_fauna = 4 
               """)
koneksi.commit()

# cek apakah data berhasil diubah atau belum
if kursor.rowcount > 0: # cek berdasarkan adanya baris atau tidak
    print(f"Data berhasil Diubah!")
else:
    print(f"Tidak ada data dengan ID tersebut!")
    
    
koneksi.close()