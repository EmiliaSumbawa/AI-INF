#Emilia Santini
#211001035
import os
os.system('cls')
judul="PROGRAM GAJI PEGAWAI"
print(judul.center(70))

nama=input("Nama Karyawan\t: ")
gaji_pokok=float(input("Gaji Pokok\t: "))
anak=int(input("jumlah anak\t: "))

tunjangan_kesejateraan=gaji_pokok*20/100
tunjangan_keluarga=(gaji_pokok*10/100)*anak
gaji_kotor=gaji_pokok+tunjangan_kesejateraan+tunjangan_keluarga
pajak=gaji_kotor*10/100
print("-"*(70))
print("Gaji Pokok\tT.Kesejateraan\tT.Keluarga\tPajak")
print(f"{gaji_pokok}\t{tunjangan_kesejateraan}\t\t{tunjangan_keluarga}\t\t{pajak}")
print("-"*(70))
print("Gaji Kotor\t: "+str(gaji_kotor))
print("Gaji Bersih\t: "+str(pajak))


