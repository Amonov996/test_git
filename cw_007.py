#  Matn ichidagi spacelarni ikkiga ko'paytirish
text = """Here, Python's ternary or conditional operators are operators that evaluate
something based on a condition being true or false. They are also known as 
conditionalexpressions. To further simplify it,
ternary operators can be thought of as one-line versions of the if-else statements."""

matn=str()

for i in text:
    matn+=i
    if i==" ":
        matn+=i*2
print(matn)

