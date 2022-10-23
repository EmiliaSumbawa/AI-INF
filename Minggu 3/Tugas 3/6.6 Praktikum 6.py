import random
import os
os.system('cls')
x=random.randint(0, 10)

pilihan = 0
while pilihan == 0:
    tebak=int(input("Masukkan angka tebakan: "))
    if tebak == x:
        print("Tebakan anda benar!")
        break
    elif tebak > x:
        print("Tebakan anda terlalu besar")
    else: 
        print("Tebakan anda terlalu kecil")