def myFun(x,y):
    x = [12, 22, 33]
    x=x.append(333)

    y=y+'will try to change this as well'


lst=[3,2,3,4,5]
y="imutable"
print("before call :",lst)
print(y)
myFun(lst,y)
print("after call",lst)# call by refrence
print(y)# call by value

def connBreak(x):
    x=[4,5,6,7,8,3]  # connection breaks as soon as we assign new obj to x
    x[0]=898



y=[55,77,88,99,22]
print(y)
connBreak(y)
print(y)


string='nameis'
print("before doing anything :",string)
string1=string
print("after assignment of :",string,"and",string1)
string1=string1+'devesh'
print('after change :',string,"and",string1)


