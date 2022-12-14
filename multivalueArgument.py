# def mulValue(**x):
#     for i in x.items():
#         print(i)
#
#
# mulValue(x='3223',y='helo')
#
# def mulValue(*x):
#     for i in x:
#         print(i)
#
# mulValue('3223','helo')
count=20
c=23
def gloablLocal(c):
    count=10
    cr=count+c
    print(cr)


gloablLocal(c)
print(count+c)


def checkGlobal():
    global count
    count=count+2
    print(count)

checkGlobal()

print(count)


def minus():
    return lambda a,b:a-b

f=minus()
print(f(33,12))


def checkMultiple(x):
    return lambda a:x%a==0 if True else False


f=checkMultiple(10)
# now will pass the multiple to lambda to check if thats a multiple of x or mot

print(f(2))

listt=[12,22,33,44,55]
print("before execution:",listt)
def globalList(ls):
    #ls=[]
    for i in range(len(ls)):
        ls[i]+=12
    #print("inside the function",ls)
    return ls
globalList(listt)
print("post function call :",listt)

