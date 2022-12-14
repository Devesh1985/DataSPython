# for num in range(-2,-5,-1):
#     print(num,end=",")
#
# for num in range(2, 5, 1):
#         print(num, end=",")

def myFun(x):
    x=[20,30,40]

    print(x)

lst=[10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


def swap(x,y):
    temp=x
    x=y
    y=temp
    c=(x,y)
    return c

def resSwap(a,b):
    print(swap(a,b))

resSwap(90,77)

