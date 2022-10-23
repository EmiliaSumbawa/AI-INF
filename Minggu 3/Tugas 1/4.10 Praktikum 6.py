#Emilia Santini
#211001035
import os
os.system('cls')
nilai=int(input("Nilai uang = "))
ribuan=nilai/1000
ribuan=int(ribuan)
praribuan=nilai-ribuan*1000
ratusan=praribuan/200
ratusan=int(ratusan)
praratusan=praribuan-ratusan*200
puluhan=praratusan/50
puluhan=int(puluhan)
print(f"{nilai} rupiah = {ribuan} (Seribuan) + {ratusan} (dua ratusan) + {puluhan} (Lima Puluhan)")