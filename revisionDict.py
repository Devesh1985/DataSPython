dict1={1:'hello',2:'new',3:'python',4:'devesh',5:'will',6:'dataengineer'}
print(dict1)
#dict1={}
#print(dict1)

l1=[3,4,5,6]

#methods
print(dict1.items())
dict1.update()
print(dict1)

dict1.update({2:'hero'})
print(dict1)

#accessing list items
print(dict1.get(2))

dict1.pop(2)
print(dict1)
#print(dict1.popitem())
print(dict1[1])

#dict1.clear()

#res=2.300+4.5
#print(f'{res:.2f}')

for i in dict1.items():
    print(i)

dict2=dict1.copy()
print("this is copied list :",dict2)

for i in dict1.items():
    print(i)

dict3={1:'hello',2:'new',3:'python',4:'devesh',5:'will',6:'dataengineer'}
#del dict3
#print(dict3)
#dict3.clear()
print(dict3)
#del(dict3[0:5])
print(dict3)

dict3.get(1)


student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}

del student[2]['age']
print("this is after del :",student)

print(student[1]['age'])
print(student[1])



sampleDict = dict([('first', 1),('second', 2),('third', 3)])
print(sampleDict)

d=dict()
for x in enumerate(range(2)):
    d[x[0]]=x[1]
    d[x[0]+7]=x[0]
    print("check this out :", d[x[0]],x[0])
    print("this is :",x[1])


d1=dict()
for x in enumerate(range(2)):
    d1[x[0]]=8
    print("this is d1 :",d1[x[0]],"this is x :",x[0],x[1],"this is x :",x)
    print(d1)
   # print(x[1])
# 0:(0,0),1:(1,1)
# x[0]=x[1]
# D = {1 : {'A' : {1 : "A"}, 2 : "B"}, 3 :"C", 'B' : "D", "D": 'E'}
# print(D[D[D[1][2]]], end = " ")
# print(D[D[1]["A"][2]])

# D[1][2]="B"
# D[D["B"]]="D"
# D["D"]='E'
#
# D[1]["A"][2]={1,"A"},"B"
# D[{1,"A"},"B"]

# D = dict()
# for i in range (3):
#     for j in range(2):
#         D[i] = j
# print(D)

# D = dict()
# for x in enumerate(range(2)):
#     D[x[0]] = x[1]
#     D[x[1]+7] = x[0]
# print(D)

dict={1:'hello'}
print(all(dict))

print(help(all))