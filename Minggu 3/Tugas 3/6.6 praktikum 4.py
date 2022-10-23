#Emilia Santini
#211001035
import os
os.system('cls')

x=int(input("Masukkan bilangan :"))
y=int(input("Masukkan pangkat :"))
jumlah=1
for i in range(y):
    jumlah=jumlah*x

print(f"{x}^{y}={jumlah}")