tup1=(4,6,7,8,9,12,44)
iteration=iter(tup1)

for index,value in enumerate(iteration):
    print(value)
    if index>3:
        break
print("this is with iter :",next(iteration))
print(next(iteration))

