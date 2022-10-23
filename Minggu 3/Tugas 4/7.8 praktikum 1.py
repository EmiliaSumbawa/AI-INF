#Emilia Santini
#211001035
import os
os.system('cls')

list1=[]
list2=[]
print("-"*70)
jml=0
for i in range(5):
    nama=input("Masukan Nama :")
    nilai=int(input("Masukan Nilai :"))
    print("-"*70)
    jml=jml+nilai
    list1.append(nama)
    list2.append(nilai)

print("-"*70)
print(f"No\tNama\t\tNilai")
print("-"*70)
for i in range(5):
    print(f"{i+1}\t{list1[i]}\t\t{list2[i]}")
print("-"*70)
print("Jumlah Mahasiswa = ", len(list1))
print("Rata-rata = ", jml/len(list1))
