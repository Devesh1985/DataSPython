x=0
while x<10:
    print(x)
    x+=1

for i in range(0,6):
    print( )
    for j in range(1,i+1):
        print(j,end="")


#total no of digits
digit=int(input("enter number"))
digiList=list(str(digit))
count=len(digiList)
print(count)
