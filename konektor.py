import mysql.connector

# Koneksi ke server MySQL
db = mysql.connector.connect(
    host="localhost",
    user="riyanadi",
    passwd="riyanadi1208",
    database="sekolah"
)



# import mysql.connector

# # Koneksi ke server MySQL
# db = mysql.connector.connect(
#     host="localhost",
#     user="riyanadi",
#     passwd="riyanadi1208",
#     database="sekolah"
# )

# cursor = db.cursor()

# idUser = 2000018289
# username = "farhan"
# psd = "password"
# namaLengkap = "Farhan Ali"
# date = 2002-10-10
# addres = "Sragen"

# # Definisikan parameter
# values = (idUser, username, psd, namaLengkap, date, addres)


# # Masukkan parameter ke dalam statement SQL menggunakan persentase sebagai placeholder
# query = "INSERT INTO 'user' ('id', 'username', 'password', 'nama', 'ttl', 'alamat') VALUES ('190002012', 'Fahrizal', 'password', 'Fahrizal Putra', '2022-12-06', 'Sragen')"

# # Jalankan statement SQL
# cursor.execute(query, values)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Commit perubahan ke database
# db.commit()

# # Menutup kursor dan koneksi
# cursor.close()
# db.close()


# import mysql.connector

# # Koneksi ke server MySQL
# cnx = mysql.connector.connect(
#     host="localhost",
#     user="riyanadi",
#     passwd="riyanadi1208",
#     database="sekolah"
# )

# # Membuat kursor
# cursor = cnx.cursor()

# # Mengeksekusi perintah SELECT
# cursor.execute('SELECT * FROM user')

# # Mengambil hasil eksekusi
# results = cursor.fetchall()

# # Menampilkan hasil eksekusi
# for row in results:
#     print(row)

# # Commit perubahan ke database
# cnx.commit()

# # Menutup kursor dan koneksi
# cursor.close()
# cnx.close()
