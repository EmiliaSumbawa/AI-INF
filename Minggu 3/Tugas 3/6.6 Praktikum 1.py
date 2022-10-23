#Emilia Santini
#211001035
import os
os.system('cls')
batas_akhir=int(input("MASUKAN BATAS AKHIR : "))
satuan=0
harga=0
print("-"*30)
print("|satuan\t     | \tHarga\t     |") 
print("-"*30)
for i in range(batas_akhir):
    satuan=satuan+0.5
    harga=(i+1)*800
    print("|   ",satuan,"    |    ",harga , "   |")

    print("-"*30)