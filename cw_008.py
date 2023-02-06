num = int(input("Son kirit: "))

for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        if i%2==0:
            print("*",end=" ")
        else:
            print("o",end=" ")
    print("")

de=num/2
for i in range(int(de/2)):
    print(" "*int(de), "#"*int(de))

print("")
    
#  Bir qatorli 
a=0
for i in range(num):
    print(" "*(num-i-1), "o"*(a+i+1))
    a+=1
    
for i in range(int(de/2)):
    print(" "*int(de+1), "#"*int(de))