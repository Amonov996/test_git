# Matn ichidagi neg uzun so'zni aqniqlash
text = """Here, Python's ternary or conditional operators are operators that evaluate
something based on a condition being true or false. They are also known as 
conditionalexpressions. To further simplify it,
ternary operators can be thought of as one-line versions of the if-else statements."""

lstText = text.split()
p=str()
c=0
for i in lstText:
    if len(i)>c:
        c=len(i)
        p=i

print(p)