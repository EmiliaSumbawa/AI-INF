#Emilia Santini
#211001035
import os
os.system('cls')

judul="DATA PEGAWAI"
print(judul.center(70))
print("-"*(70))


nama=input("\tNama\t       : ")
golongan=input("\tGolongan       : ")
t_jam_kerja=float(input("\tTotal Jam Kerja: "))

if golongan=="A" :
    gaji_pokok=500000
    tunjangan=10/100*gaji_pokok
    lembur=5000
elif golongan=="B":
    gaji_pokok=700000
    tunjangan=15/100*gaji_pokok
    lembur=10000
elif golongan=="C":
    gaji_pokok=900000
    tunjangan=10/100*gaji_pokok
    lembur=5000
else:
    print("Golongan yang anda masukan tidak terdaftar")
    gaji_pokok=0
    tunjangan=0
    lembur=0

if t_jam_kerja>200:
    jam_lembur=t_jam_kerja-200
    uanglembur=jam_lembur*lembur
else:
    lembur=0
    uanglembur=0
print("-"*(70))

judul="PERHITUNGAN GAJI"
print(judul.center(70))
print("-"*(70))


gaji=gaji_pokok+tunjangan+uanglembur

print("\tgaji_pokok: "+str(gaji_pokok))
print("\ttunjangan : "+str(tunjangan))
print("\tlembur    : "+str(lembur))
print("-"*(70))
print("\tTotal :"+str(gaji))
