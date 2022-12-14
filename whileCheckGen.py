def test():
    n=5
    while n:
        yield n
        n-=1

for i in test():
    print(i)


def funLength(*name):
    for i in name:
        print(i)

funLength('hero','ram','new','raja')

a='devesh'
def stringCon():
    ls=list(a)
    print(ls)
    count=len(ls)//2
    ls.insert(count,'ram')
    print("".join(ls))


#Create a new string made of the first, middle, and last characters of each input string
res=[]
num=int(input("enter range"))
for i in range(num):
    string=input("enter string\n")
    res.append(string)
print(res)
ele=""
for i in range(len(res)):
    ele=ele+res[i][0]
print(ele)




stringCon()