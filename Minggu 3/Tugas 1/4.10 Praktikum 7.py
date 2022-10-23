import os
os.system('cls')

gaji=float(input("gaji\t\t= "))
hutang=float(input("hutang\t\t= "))
jumlah=gaji-hutang
sehari_hari=jumlah*70/100
tabung=jumlah*20/100
infak=jumlah*10/100
print ("Biaya sehari hari= "+str(sehari_hari))
print("Tabungan\t= "+str(tabung))
print("infak\t\t= "+str(infak))

