#print("Hello {} {}! You just delved into python."){first}
first='devesh'
last='joshi'
print(f'my name is {first} {last}')

print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))
print("Total students : %3d, Boys : %2d" % (240, 120))

string=input("enter char : \n")
position=int(input("enter the index : \n"))
character=input("enter char to add : \n")
Nstr=string[:position]+character+string[position+1:]
print(Nstr)

