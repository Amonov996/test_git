# Kiritilgan sonni indexlar darajasiga ko'paytirish
sn = int(input("Son kirit: "))

j=0
sum=0

for i in str(sn):
    j+=1
    print(f"{i} ^ {j} = {int(i)**j}")
    sum+=int(i)**j
    
print(f"Umumiy qiymat {sum}")