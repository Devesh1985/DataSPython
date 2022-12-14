# in python there are two type os arguments we can pass to a function
# 1 non keyword argument
# 2 keyword argument

# non keyword argument
def concat(x,y):
    res=x+y
    return res

print(concat('he is ',y='hero'))

#keyword argument

def student(firstname,lastname):
    res=(f"lastname of {firstname} is {lastname} ")
    print(res)# either return or print here in thie location only

student(firstname='raja',lastname='ambani')


# Variable length argument
# we can pass a variable number of argument to a function with the help of two special symbols
#  * and **

# non keyword argument

def lsiww(*argv):
    for lis in argv:
        print(lis)

lsiww('he','she','log','start')

# keyword length argument

def dictExa(**kwargs):
    dictExam={}
    for key,value in kwargs.items():
        print(key,value)


dictExa(name='devesh',game='yogesh')


