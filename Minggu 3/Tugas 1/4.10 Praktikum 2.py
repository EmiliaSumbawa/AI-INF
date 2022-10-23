data=("DATA KECEPATAN MOBIL")
garis1=("-----------------------------")
kecepatan=input("Kecepatan rata-rata (km/jam)     :"&kecepatan)
waktu=input("Waktu tempuh (jam)      :"&waktu)
jarak=kecepatan*waktu
jarak=("Jarak tempuh                 :")
garis2=("-----------------------------")
 
print(data.center(100))
print(garis1.center(50))
print(kecepatan.center(50))
print(waktu.center(50))
print(jarak.center(50))
print(garis2.center(50))