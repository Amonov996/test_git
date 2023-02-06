# Kiritilgan matn harflarnini ajratish
text = input("Matn kiriting: ")

lower = str()
upper = str()
symbol = str()
number = str()

for i in text:
    if i.islower():
        lower+=" "+i
    elif i.isupper():
        upper+=" "+i
    elif i.isdigit():
        number+=" "+i
    else:
        symbol+=" "+i

print(f"lower = {lower}")
print(f"upper = {upper}")
print(f"symbol = {symbol}")
print(f"number = {number}")
