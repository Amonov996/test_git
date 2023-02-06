lst = [[1,2,],[0,9,9],[9,7,0],[0],[0,0],[4,3]]
maxNum = int()
maxLst = list()

for i in lst:
    temp=0
    for j in i:
        temp=temp+j
        if temp>maxNum:
            maxLst = i
            maxNum = temp
print("maxNum",maxNum)
print("maxLst", maxLst)
        
# Done    