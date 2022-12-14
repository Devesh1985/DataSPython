import itertools

a=[1,3,5,7,10]
b=[1,2,6,8,9]
for i in zip(a,b):
    print(i)

# zip will produce tuple with single iterable incase you provide one iterable parameter
a=[1,3,5,7,10]
#b=[1,2,6,8,9]
for i in zip(a):
    print(i)

#by default zip will execute till the shortest iterable length, however if you need to execute this for longest iterable
#length we can use

a=[3,5,6,7,8,9]
b=[44,55]

for i in itertools.zip_longest(a,b,fillvalue='-'):
    print(i)



