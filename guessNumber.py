# take a number

number = 18
#take input
num = int(input("you have 6 attempt to guess the correct number, Please enter your guess""\n"))
count=6
while count>0:
    if num == number:
        print("your guess is correct Congratulations!, you took",(count),"no of guesses")
        break
    elif num > number:
        print("you need to enter small number,you have" ,(count-1),"attempt remaining post this")
        num=int(input("Please retry :"))
        count -= 1
    elif num < number:
        print("you need to increase the value of the number,you have" ,(count-1),"attempt remaining post this")
        num=int(input("Please retry :"))
        count -= 1

print("sorry you have reached maximum retries limit")







