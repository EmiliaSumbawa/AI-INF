#Emilia Santini
#211001035
import os
os.system('cls')
print("-"*(70))

e=int(input("Masukan nilai 1 = "))
m=int(input("Masukan nilai 2 = "))
i=int(input("Masukan nilai 3 = "))

if e == m and e == i and m==i:
    print("Nilai ketiga bilangan sama = "+str(e))
elif e==m:
     print("Nilai kedua bilangan sama = "+str(m))

elif e==i:
    print("Nilai kedua bilangan sama = "+str(i))
elif m==i:
    print("Nilai kedua bilangan sama = "+str(i))
else:
    print("nilai tidak ada yang sama ")
    