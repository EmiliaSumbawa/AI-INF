#Emilia Santini
#211001035
import os
os.system('cls')

list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
jml1=0
jml2=0
jml3=0
jml4=0

print("-"*70)

jumlah=int(input("Jumlah Mahasiswa :"))
for i in range(jumlah):
    nama=input("Nama Mahasiswa :")
    Tugas=int(input("Masukan nilai Tugas :"))
    uts=int(input("Masukan nilai UTS :"))
    uas=int(input("Masukn nilai UAS :"))
    nilai_akhir=30/100*Tugas+30/100*uts+40/100*uas
    jml1+=Tugas
    jml2+=uts
    jml3+=uas
    jml4+=nilai_akhir
    list2.append(nama)
    list3.append(Tugas)
    list4.append(uts)
    list5.append(uas)
    list6.append(nilai_akhir)
    print()
   
print("Nilai akhir :"+str(nilai_akhir))

print("-"*70)
list1.append(jumlah)
list2.append(nama)
list3.append(Tugas)
list4.append(uts)
list5.append(uas)
list6.append(nilai_akhir)

print(f"No\tNama\tTugas\tUTS\tUAS\tNA")
print("-"*70)
for i in range(2):
    print(f"{i+1}\t{list2[i]}\t{list3[i]}\t{list4[i]}\t{list5[i]}\t{list6[i]}")

print("-"*70)
print("Rata-rata Tugas = ", jml1/jumlah)
print("Rata-rata UTS = ", jml2/jumlah)
print("Rata-rata UAS = ", jml3/jumlah)
print("Rata-rata Nilai = ", jml4/jumlah)



