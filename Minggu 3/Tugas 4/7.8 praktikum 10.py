#Emilia Santini
#211001035
import os
os.system('cls')

list1=[]
list2=[]

banyak=int(input("Masukkan banyak data: "))
for i in range(banyak):
    bilangan=int(input("Masukkan bilangan: "))
    if bilangan>0:
        list1.append(bilangan)
    else:
        list2.append(bilangan)
    
if len(list1) > len(list2):
    print("Bilangan positif lebih bnyk")
else:
    print(("Bilangan negatif lebih banyak"))
    