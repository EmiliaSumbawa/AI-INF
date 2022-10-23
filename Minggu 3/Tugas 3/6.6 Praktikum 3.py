#Emilia Santini
#211001035
import os
os.system('cls')

jum=0
n=int(input("Masukkan banyak data: "))
for i in range(n):
    nilai=int(input(f"Masukkan nilai ke {i+1} : "))
    jum=jum+nilai

rata=jum/n
print(f"Total Nilai : {jum}")
print(f"Rata-rata : {rata}")
