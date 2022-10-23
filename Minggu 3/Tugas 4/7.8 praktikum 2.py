#Emilia Santini
#211001035
import os
os.system('cls')

list1=[]
list2=[]
list3=[]
print("-"*70)
jml=0
lulus=0
tdk_ll=0
for i in range(5):
    nama=input("Masukan Nama :")
    nilai=int(input("Masukan Nilai :"))
    if nilai>=60:
        grade="Lulus"
        lulus+=1
    else :
        grade="Tidak Lulus"
        tdk_ll+=1
    print()
    jml=jml+nilai
    list1.append(nama)
    list2.append(nilai)
    list3.append(grade)

print("-"*70)
print(f"No\tNama\t\tNilai\tKeterangan")
print("-"*70)
for i in range(5):
    print(f"{i+1}\t{list1[i]}\t\t{list2[i]}\t{list3[i]}")


print("-"*70)
print("Jumlah Mahasiswa = ", len(list1))
print("Rata-rata = ", jml/len(list1))
x=max(list2)
y=min(list2)
print("Nilai Terendah: ", y)
print("Nilai Tertinggi: ", x)
print("Jumlah Lulus: ", lulus)
print("Jumlah Tidak Lulus: ", tdk_ll)
