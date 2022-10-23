#Emilia Santini
#211001035
import os
os.system('cls')

def persegi_panjang():
    p=int(input("Masukkan panjang = "))
    l=int(input("Masukkan lebar = "))
    luas=p*l
    print("Luas = ", luas)
def segitiga():
    a=int(input("Masukkan Alas = "))
    t=int(input("Masukkan tinggi = "))
    luas=(1/2)*a*t
    print("Luas = ", luas)
def Lingkaran():
    r=int(input("Masukkan jari-jari = "))
    luas=3.14*r*r
    print("Luas = ", luas)

print("""
Pilihan: 
1. Persegi Panjang
2. Segitiga
3. Lingkaran
""")
pilihan=input("Masukkan Pilihan: ")
pilihan=pilihan.upper()

if pilihan == "PERSEGI PANJANG":
    persegi_panjang()
elif pilihan == "SEGITIGA":
    segitiga()
elif pilihan == "LINGKARAN":
    Lingkaran()




