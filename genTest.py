def genCheck():
    #print('hello')
    num=8
    while num<10:
        if num%2==0:
            yield num
        num+=1


print(next(genCheck()))
#print(next(ls1))

