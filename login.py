import os
import time
from konektor import db
import getpass
import mysql.connector

cursor = db.cursor()

def login(nama, psd):
    # cek = False
    # file = open("database.txt", "r")
    # for i in file:
    #     username,psd,roles = i.split(",")
    #     psd = psd.strip()
    #     if(username == nama and psd==password):
    #         cek = True
    #         break
    # file.close()
    # if(cek==True):
    #     print("Login berhasil, silahkan masuk!")
    # else:
    #     print("nama atau password anda salah ! atau")
    #     print("anda belum terdaftar, silahkan daftar !")
    #     time.sleep(2)
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     awal()
    username = nama
    password = psd

    query = "SELECT * FROM user WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    # Jika ada data yang cocok, login berhasil
    if cursor.fetchone():
        print("Login berhasil!")
    else:
        print("Username atau password salah!")


def register(nama, password, role):
    file = open("database.txt", "a")
    file.write(nama + ", " + password + "," + role + "\n")

def masuk(option):
    global nama
    if(option==1):
        nama = input("Masukkan nama anda : ")
        password = getpass.getpass()
        login(nama, password)
    else:
        # print("Masukkan ID dan password anda yang baru !")
        nama = input("Masukkan nama anda : ")
        password = input("Masukkan password anda : ")
        role = input("Masukkan role anda : ")
        register(nama, password, role)
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





