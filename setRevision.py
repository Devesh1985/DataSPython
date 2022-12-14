#set

# listA=[3,2,4,2,]
# print(3 in listA)
#
# dictA={1:'hello',(2,3):'new','ramji':'jai shree ram'}
# print(dictA)
# print('ramji' in dictA)
#
# tup=(3,2,3,4,88)
# print(2 in tup)
setA={3,4,5,6,7,8,9,11}
print(setA)

#ele=set(input("enter set :").split())
ele={5,3,2,1,6,7,8,89}
print(ele)
print(setA.intersection(ele))
#print(setA)
#print(ele)

#print(setA.intersection_update(ele))
#print(setA)
# insertion update will update the old set with the result and no return type

#setA.remove(3)
#print(setA)

print(setA.difference(ele))
#exta ele from setA which are not in ele
#setA.difference_update() # update the old set with result

print(setA.issubset(ele))
print(setA.issuperset(ele))
print(setA.isdisjoint(ele))
#returns true if both the sets have nothing in common

print(setA.symmetric_difference(ele))
#print ele which are unique in both the sets
print(setA)
setA.discard(2)# will remove the element from set but not throw error if ele not present
print(setA)


