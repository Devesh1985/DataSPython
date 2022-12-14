# generate multiple of 12

def multiple():
    i=1
    while True:
        yield 12*i
        i+=1

for i in multiple():
    if i>120:
        break
    else:
        print(i)

def revive():
    while True:
        userInput=input("enter y for yes and n for no : ")
        if userInput.lower()=='y':
            return (1)
        else:
            if userInput.lower()=='n':
                return (0)


if revive():
    print("yes")
else:
    print("no")




