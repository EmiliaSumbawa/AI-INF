list1=[]
banyak=int(input("Masukkan berapa banyak data: "))
for i in range(banyak):
    bilangan=int(input("Masukkan bilangan: "))
    if bilangan%3==0 and bilangan%2==1:
        list1.append(bilangan)

print(list1)