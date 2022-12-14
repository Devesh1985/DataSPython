# Enter your code here. Read input from STDIN. Print output to STDOUT
s1=7
s2=21
j=0
pr=s1
count=(s2//2)-1
m=1
for i in range(((s1//2)+1)): # coloums
    #print()
    if (i==(s1-1)//2): # welcome test
    #if count <1:
       print('-'*(s1)+'WELCOME'+'-'*(s1))
       break
    for j in range(count): #  printing rows left top area
        print('-',end="")
    print('.|.'*m,end="")
    for k in range(count): # print rows right toop area
        print('-',end='')
    print()
    count = count - 3
    m = m + 2
count=3

mul=s1-2
for i in range((s1//2)):#  coloumns bottom area
    #print()
    for j in range(count):# rows left bottom area
         print('-',end="")
    print('.|.' * ((mul)),end="")
    for k in range(count): # rows right bottom area
        print('-',end='')
    print()
    mul = mul - 2
    count=count+3




















