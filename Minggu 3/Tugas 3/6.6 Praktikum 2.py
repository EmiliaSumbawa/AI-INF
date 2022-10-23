#Emilia Santini
#211001035
import os
os.system('cls')

nilai_awal=int(input("Masukan Nilai awal :"))
banyak_suku=int(input("Cari Suku ke:"))
rasio=int(input("Rasio :"))

for i in range(banyak_suku):
    print(f"Suku ke {i+1} : {nilai_awal}")
    nilai_awal*=rasio