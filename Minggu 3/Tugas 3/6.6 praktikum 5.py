#Emilia Santini
#211001035
import os
os.system('cls')

nilai=int(input("Masukkan nilai faktorial (!) ="))
faktorial=1
for i in range(1, nilai+1):
    faktorial*=i
print(f"{nilai}! = {faktorial}")