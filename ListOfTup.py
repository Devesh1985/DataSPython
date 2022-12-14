#create a list of touples from user input

ex=[(2,3,4),(4,5,6),(4,5,6),(4,5,6),(2,3,4)]
ex1=set(ex)
ex2=list(ex1)
print(ex2)

tup=((2,3,4),(4,8,6),(4,9,6),(4,5,6),(2,3,4))
print(tup[3],tup[-4])

##Write a Python program to convert a tuple to a string.
tup2=('test','hello','noe',3,6)
strR=""
for i in tup2:
    strR=strR+str(i)
print(strR)
print(type(strR))

tup33 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str=tup33
str=''.join(tup33)
#print(str)

repeated=[]
single=[]
tup44=('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
print('c' in tup44)
for i in tup44:
    if i not in single:
        single.append(i)
print(single)


list23=[3,4,5,'list','new']
tou23=tuple(list23)
print(type(tou23))

t22=(1,2,3,4,5,6)
print(t22[::-1])
print(t22)
print(t22.index(3))




