# List ichidagi bo'sh listlarni o'chirish

lst = [[],[1,2,3],[4,3,[]],[],[3,2,0]]
# lst = [x for x in lst if x!=[]]
lst2 = list()
print(lst)
for i in lst:
    if i!=[]:
        lst2.append(i)
       
print(lst2)
# Half of problem is done