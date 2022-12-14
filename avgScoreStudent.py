import itertools
# a=[23,44,56,78,99]
# b=[11,22,33,44,55]
# c=[]
# print(type(c))
# for i in zip(a,b):
#     c.append(i)
# c=dict(c)
# print(c)
#========================


res=[]
n,x=list(map(int,input().split(" ")[:2]))
print(n,x)
for st in range(x):
    mr=list(map(float,input().split(" ")[:n]))
    print(mr)
    res.append(mr)
for i in zip(*res):
   avg=0
   for j in i:
       print(j)
       avg=j+avg
       fav=avg/3
   print(f"{fav:.02f}")





   #================================
# for i in res:
#     jsum = 0
#     avg = 0
#     lstAvg=[]
#     for j in i:
#         jsum = j + jsum
#         avg = jsum / len(i)
#     lstAvg.append(avg)
#     print(avg,end=" ")

# res=[[12.0, 12.0],[13.0, 13.0],[14.0, 1.0]]
# ss=tuple(res)
# print(ss)
# res=zip([12.0, 12.0],[13.0, 13.0],[14.0, 1.0])
# for i in res:
#     print(i)

# res=[[12.0, 12.0],[13.0, 13.0],[14.0, 1.0]]
# for i in zip(*res):
#     print(i)

    # ss=",".join(i)
    # print(ss)


# for i in ss:
#     print(i)



















