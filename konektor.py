import mysql.connector

# Koneksi ke server MySQL
db = mysql.connector.connect(
    host="localhost",
    user="riyanadi",
    passwd="riyanadi1208",
    database="sekolah"
)