from login import awal
from KHS import KHS
from Pembayaran import pembayaran
from Presensi import Presensi
from Praktikum import Praktikum

def dashboard():
    awal()
    print("+---------------------------------------+")
    print("| SELAMAT DATANG DI PORTAL SMK 2 SRAGEN |")
    print("+---------------------------------------+")
    print("1. Pembayaran SPP")
    print("2. KHS")
    print("3. Presensi")
    print("4. Praktikum")
    menu = int(input("Masukkan pilihan anda : "))
    if(menu==1):
        pembayaran()
    elif(menu==2):
        KHS()
    elif(menu==3):
        Presensi()
    elif(menu==4):
        Praktikum()

dashboard()
