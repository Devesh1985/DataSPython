def stringCunt(st,string):
    slen=len(st)
    count=0
    j=0
    while j<len(string):
        if st in string[j:slen]:
            count+=1
            print(count,st)
        #print(string[j:slen])
        j+=1
        slen+=1

s="BANANA"
for i in range(1,len(s)+1):
    rs=s[0:i]
    print("befor call :",rs)
    if rs!=" ":
        stringCunt(rs,s)



#     if a in str1
# while j<len(str1):
#     if a in str1:
#         count+=1







