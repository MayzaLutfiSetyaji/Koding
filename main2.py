#mengimport modul bawaan "random"
import random

angka_rahasia  = random.randint(1, 100)
tebakan = 0

print("Selamat datang pada tebak angka random")
print("Pilih sebuah angka dari angka 1 sampai 100")

while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan angka: "))

    if tebakan < angka_rahasia:
        print("Angka terlalu kecil!!")
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar!!")
    else:
        print("Selamat, tebakan anda benar")
