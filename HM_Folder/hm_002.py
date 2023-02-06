lst = ["Alo", "salom", "Haydar", "Arsenal", "Eng uzun gap", "gap"]
maxLst = str
m=0
for i in lst:
    if len(i)>m:
        m = len(i)
        maxLst=i
    
print(maxLst)

# Done