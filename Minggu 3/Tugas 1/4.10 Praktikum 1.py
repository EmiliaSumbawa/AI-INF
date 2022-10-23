#Emilia Santini
#211001035
import os
os.system('cls')
h="PROGRAM MENGHITUNG PEMBELIAN"
garis="-"*100
print(h.center(100))
print(garis)

harga=12000
print("Harga satuan\t\t: Rp. "+str(harga))  
Jumlah_pembelian=input("Jumlah pembelian\t: ")
discon=harga*0.2
print("Discon\t\t\t: "+str(discon))
harga_total=int(harga)*int(Jumlah_pembelian)-discon
print("Harga Total\t\t: "+str(harga_total))
print("-"*100)

