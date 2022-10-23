#Emilia Santini
#211001035
import os
os.system('cls')

pilihan=int(input("Masukan pilihan anda: 1. Ganjil / 2.Genap :"))
awal=int(input("masukan bilangan awal:"))
akhir=int(input("masukan bilangan akhir:"))

if pilihan==1:
    for x in range(awal,akhir+1):
        if x % 2==1:
            print(x)
            
else:
    for x in range(awal,akhir+1):
        if x%2==0:
            print(x)