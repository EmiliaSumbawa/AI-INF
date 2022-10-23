#Emilia Santini
#211001035
import os
os.system('cls')
judul="PROGRAM MENGHITUNG TAGIHAN TELEPON"
garis="-"*100
print(judul.center(100))
print(garis)
print("\tDATA PELANGGAN")
nama=input("\tNama Pelanggan\t: ")
cakap=int(input("\tPercakapan\t: "))
sms=int(input("\tSMS\t\t: "))
print()
abn=20000
rp_cakap=1000*cakap
rp_sms=300*sms
tagih=abn+rp_cakap+rp_sms
print("\tTAGIHAN")
print(f"\tAbonemen\t\t: Rp {abn}")
print(f"\tBiaya Percakapan\t: Rp {rp_cakap}")
print(f"\tBiaya SMS\t\t: Rp {rp_sms}")
print(f"\tTotal Tagihan\t\t: Rp {tagih}")
print(garis)