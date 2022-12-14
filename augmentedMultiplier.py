number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    answer+=number

print(answer)


# check if first non devisible by 5
lst=[5,10,15,20,25]
for i in lst:
    if i>5 and i%5!=0:
        print("{} is the first number in the list".format(i))
        break
else:
    print("sorry we do not have anything which matches your criteion")
