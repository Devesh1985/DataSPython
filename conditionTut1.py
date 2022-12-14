
ls=[]
count=0
ls.append(1)
ls.append(2)
for i in range(20):
    num = 2
    while num<i:
        if i%num==0:
            break
        ls.append(i)
        break
        num+=1
print(ls)



