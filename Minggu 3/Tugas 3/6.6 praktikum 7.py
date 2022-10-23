#Emilia Santini
#211001035
import os
os.system('cls')

a=int(input("bilangan x: "))
b=int(input("bilangan y: "))
jml=0
for i in range(a, b):
    print(i+1, " ", end="")
    if i == b-2:
        break
print()