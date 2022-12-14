listA=['800','austin','rover']
listB=['100000','10000000','20000000']
dictA={}
for a,b in zip(listA,listB):
    dictA[a]=b
print(dictA)


for i in reversed(listA):
    print(sorted(listA))