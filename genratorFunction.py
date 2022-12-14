def square():
        x=1
        while True:
                yield x*x
                x+=1

for num in square():
   if num>99:
    break
    print(num)












