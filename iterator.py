tup=('2','5','9','01','88')
for i in tup:
    print(i)


ch_iter=iter(tup)
for index,i in enumerate(ch_iter):
    print('index :'+ str(index),'is :',i)

def checkIterable(ob):
    try:
        iter(ob)
        print(ob," is iterable")

    except:
        print(ob," is not an iterable")

for i in [34, [4, 5], (4, 5),
{"a":4}, "dfsdf", 4.5]:
    checkIterable(i)


def table():
    i=0
    while i<3:
        c = i * 12
        yield c
        i += 1



for i in table():
    if i>100:
        break
    print(i)




