string=input("enter the string :\n")
subString=input("enter the subString :\n")
    #print(string.count(subString))
count=0
for index,i in enumerate(string):
    str1=string[index:len(subString)+index]
    if str1==subString:
        count=count+1
    else:continue
print(count)
