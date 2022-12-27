import os
import time
from konektor import db
from pwinput import pwinput

cursor = db.cursor()

def login(nama, psd):
    username = nama
    password = psd

    query = "SELECT * FROM user WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    # Jika ada data yang cocok, login berhasil
    if cursor.fetchone():
        print("Login berhasil!")
    else:
        print("Username atau password salah!")
        print("anda belum terdaftar, silahkan daftar !")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        awal()


def register(name, password, nama, alamat, ttl, id):

    idUser = id
    username = name
    psd = password
    namaLengkap = nama
    date = ttl
    addres = alamat

    # Definisikan parameter
    values = (idUser, username, psd, namaLengkap, date, addres)

    # Masukkan parameter ke dalam statement SQL menggunakan persentase sebagai placeholder
    query = "INSERT INTO `user` (`id`, `username`, `password`, `nama`, `ttl`, `alamat`) VALUES (%s, %s, %s, %s, %s, %s)"

    # Jalankan statement SQL
    cursor.execute(query, values)

    # Commit perubahan ke database
    db.commit()

    # Menutup kursor dan koneksi
    cursor.close()
    db.close()


def masuk(option):
    if(option==1):
        nama = input("Masukkan nama anda : ")
        password = pwinput("Masukkan password anda : ", "*")
        login(nama, password)
    else:
        # print("Masukkan ID dan password anda yang baru !")
        id = input("Masukkan id anda : ")
        name = input("Masukkan username anda : ")
        password = pwinput("Masukkan password anda : ", "*")
        nama = input("Masukkan nama anda : ")
        ttl = input("Masukkan tanggal lahir : ")
        alamat = input("Masukkan alamat anda : ")
        register(name, password, nama, alamat,ttl, id)
        print("Anda berhasil terdaftar")
def awal():
    global option
    print("+---------+")
    print("|| LOGIN ||")
    print("+---------+")
    print("1. Masuk, jika sudah punya akun ")
    print("2. Daftar, jika belum punya akun")
    option = int(input("Masukkan pilihan anda : "))
    if(option!=1 and option!=2):
        print("Inputan yang anda masukkan salah, silahkan ulangi kembali")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        awal()
    else:
        masuk(option)





