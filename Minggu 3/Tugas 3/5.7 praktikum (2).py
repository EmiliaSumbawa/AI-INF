#Emilia Santini
#211001035
import os
os.system('cls')

print("-"*(70))

e=int(input("Masukan nilai 1 = "))
m=int(input("Masukan nilai 2 = "))
i=int(input("Masukan nilai 3 = "))


if e > m and e > i:
    print("nilai pertama lebih besar = "+str(e))
elif m>e and m>i:
    print("nilai kedua lebih besar = "+str(m))
else:
    print("nilai ketiga lebih besar = "+str(i))
   
      
print("-"*(70))