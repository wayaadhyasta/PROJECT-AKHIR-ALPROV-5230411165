import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

#insert data ke tabel
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('1','Harimau Jawa', 'Mamalia', 'Jawa', '40', '2019')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('2', 'Kuskus Beruang', 'Mamalia', 'Sulawesi', '30', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('3', 'Beruang Madu', 'Mamalia', 'Sumatera', '1000', '2020')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('4', 'Pesut Mahakam', 'Mamalia', 'Kalimantan', '100', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('5', 'Burung Maleo', 'Burung', 'Sulawesi', '7000', '2023')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('6', 'Macan Dahan', 'Mamalia', 'Sumatera', '400', '2020')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('7', 'Kancil', 'Mamalia', 'Jawa', '60', '2022')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('8', 'Gajah Kalimantan', 'Mamalia', 'Kalimantan', '1500', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('9', 'Elang Jawa', 'Burung', 'Jawa', '200', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA(id_fauna, nama_fauna, jenis, asal,  jml_skrg, thn_ditemukan)
                VALUES('10', 'Katak Borneo', 'Amfibi', 'Kalimantan', '2000', '2023')
                ''')
koneksi.commit()
koneksi.close()





