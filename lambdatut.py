# def summ(a,b):
#     return a+b

# summ=lambda a,b:a+b
# print(summ(9,20))

# def yesortKarega(ls):
#     return ls[0]

yesortKarega=lambda ls:ls[0]


lisst=[[4,7],[33,10],[22,10],[86,66]]
#print(yesortKarega(lisst))

# lisst.sort(key=yesortKarega)
# print(lisst)


lisst.sort(key=yesortKarega)
print(lisst)



#print(lambda x:sort)





