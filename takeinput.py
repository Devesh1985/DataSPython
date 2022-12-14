N=int(input())
listA=[]
for j in range(0,N):
    cmd=input()
    listA.append(cmd)
    print(listA)
for i in listA:
    if i=='append':
        arg=int(input()[:1])
    if i=='insert':
        arg1=int(input())
        arg1=int(input())
        listA.insert(arg1)
        print(listA)


