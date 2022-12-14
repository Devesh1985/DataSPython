string='Www.HackerRank.com presents "Pythonist 2".'
string1=""
for i in string:
    if i.islower()==True:
        string1=string1+i.upper()
    elif i.isupper()==True:
        string1=string1+i.lower()
    elif i.isspace()==True:
        string1=string1+i
    elif i.isdigit()==True:
        string1 = string1 + i
    elif i=='.' or i=='"':
        string1 = string1 + i
    else:
        string1 = string1 + i
print(string1)