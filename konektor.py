import mysql.connector

    # Koneksi ke database MySQL
db = mysql.connector.connect(
        host="localhost",
        user="riyanadi",
        passwd="riyanadi1208",
        database="sekolah"
    )

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
