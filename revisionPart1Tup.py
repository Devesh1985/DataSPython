# tuple : a set of data type can be mixed , is simmilare to list but are immutable i.e you cant change the size of a tuple
#once created

# num = tuple(input("enter tuple elements :\n").split())
# print(num)
# num3=(2,3,4,5)
# print(num.index('3'))# print the index of the give no
# num=num+num3
# print(num)
# tup2=num+num3
# print(tup2)
# print(tup2.__add__(('23665',)))

tup=('hello','2',7,9,'new')
print(tup)

print(tup[:])
#print(sorted(tup))# should be same type

tup1=('4','5','6','7')
list1=['as','dd','new']
l2=[4,5,6,7,8,9]
print(sorted(l2))
l2.reverse()

print(l2)

number=232323
print(str(number)[::-1])

list1 = ['xyz', 'yara', 'PYnative']
list2=[33,88,99]
list2[0:4]=[2,3,4,5]
print("here is the new list:",list2)
print(list2[-2])
print (max(list1))
print(max(list2))
print((max.__doc__))






