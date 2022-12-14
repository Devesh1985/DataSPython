#even num

num=10

for i in range(2,num,2):
    print(i)

#list comprhension

ls=[i for i in range(num) if i%2==0]
print(ls)

def calc(x):
    return lambda x:x+15

def calc():
    return lambda x,y:x*y
fun=calc()
print(fun(10,8))

sr=" "
st='hello 12world'
rs=st.split(" ")

for i in rs:
    sr=sr+i.capitalize()+" "
print(sr.strip())


