userInput=input("enter the values using any seprator you like :")
seprator=""
for char in userInput:
    if not char.isnumeric():
        seprator=seprator+char

num=""
values="".join(char if char not in seprator else " " for char in userInput).split()
print(sum([int(val) for val in values]))

def fetchCpaital(string):
    varCaps=""
    char=string.split()
    for ch in char:
        for c in ch:
            if c.isupper():
                varCaps=varCaps+c
    print(varCaps)





fetchCpaital("Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?")