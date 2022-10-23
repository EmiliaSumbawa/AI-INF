#Emilia Santini
#211001035
import os
os.system('cls')

judul="DATA NILAI MAHASISWA"
print(judul.center(70))
print("-"*(70))

nama=input("\tNama  : ")
Tugas=float(input("\tTugas : "))
UTS=float(input("\tUTS   : "))
UAS=float(input("\tUAS   : "))
print("-"*(70))
judul="NILAI AKHIR DAN GRADE"
print()
print(judul.center(70))
print("-"*(70))
print("\tNama : "+str(nama))
Nilai_akhir=25/100*Tugas+35/100*UTS+40/100*UAS
print("\tNilai Akhir : "+str(Nilai_akhir))

if Nilai_akhir >= 75 :
    grade="A"
elif Nilai_akhir >= 60 :
    grade="B"
elif Nilai_akhir >=45:
    grade="C"
else:
    grade="D"
print("\tGrade : "+str(grade))
print("-"*(70))

    








