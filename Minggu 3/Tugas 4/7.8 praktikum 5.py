list1=[]
bilangan=int(input("Berapa banyak data :"))


for i in range (bilangan):
    x=int(input("Masukkan bilangan: "))
    list1.append(x)

m=max(list1)
print("bilangan maximal adalah "+str(m))


