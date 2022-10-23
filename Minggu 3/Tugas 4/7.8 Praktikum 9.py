#Emilia Santini
#211001035
import os
os.system('cls')

listnilai=[]
jum=0
banyak=int(input("Masukkan banyak data: "))
for i in range(banyak):
    nilai=int(input(f"Masukkan nilai ke {i+1} : "))
    jum+=nilai
    listnilai.append(nilai)
print(f"Banyak data : {len(listnilai)}")
print(f"Penjumlahan data : {jum}")