#Emilia Santini
#211001035
import os
os.system('cls')

list1=[]
banyak=int(input("Masukkan berapa banyak data: "))
for i in range(banyak):
    bilangan=int(input("Masukkan bilangan: "))
    if bilangan%3!=0:
        list1.append(bilangan)

print(list1)