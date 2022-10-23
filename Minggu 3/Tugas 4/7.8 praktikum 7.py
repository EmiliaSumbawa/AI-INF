list1=[]
banyak=int(input("Masukkan berapa banyak data: "))
for i in range(banyak):
    bilangan=int(input("Masukkan bilang: "))
    if bilangan%5==0:
        list1.append(bilangan)

print(list1)
