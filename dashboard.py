from login import awal
from KHS import KHS
from Pembayaran import pembayaran
from Presensi import Presensi
from Praktikum import Praktikum
import time
import os

def menu():
    print("+---------------------------------------+")
    print("| SELAMAT DATANG DI PORTAL SMK 2 SRAGEN |")
    print("+---------------------------------------+")
    print("1. Pembayaran SPP")
    print("2. KHS")
    print("3. Presensi")
    print("4. Praktikum")
    print("5. Keluar")
    opsi = int(input("Masukkan pilihan anda : "))
    if(opsi==1):
        pembayaran()
    elif(opsi==2):
        KHS()
    elif(opsi==3):
        Presensi()
    elif(opsi==4):
        Praktikum()
    elif(opsi==5):
        awal()
    else:
        print("Menu yang anda masukkan salah!, coba kembali")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()

def dashboard():
    awal()
    menu()
    


dashboard()
