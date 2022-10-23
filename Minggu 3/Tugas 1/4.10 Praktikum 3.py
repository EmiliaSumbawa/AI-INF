#Emilia Santini
#211001035
import os
os.system('cls')
h="PROGRAM PENJUALAN BUKU"
garis="-"*100
print(h.center(100))
print(garis)

harga=50000
harga_satuan=input("Harga satuan         : Rp. ")
Jumlah_pembelian=input("Jumlah pembelian     : ")
discon=harga*0.5
print("Discon               : Rp. "+str(discon))
harga_total=int(harga)*int(Jumlah_pembelian)-discon
print("Harga Total          : "+str(harga_total))

garis="-"*100
print(garis)
