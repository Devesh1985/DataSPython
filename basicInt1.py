#prime number

number=int(input("enter the range""\n"))
prime=2
while prime<number:
    if number%prime==0:
        break
    elif number%prime!=0:
        continue
    print(number,"is a prime number")
    prime+=1















