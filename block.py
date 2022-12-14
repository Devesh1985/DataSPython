# name=input("enter your name :")
# age=int(input("{0} please enter your age :".format(name)))
# print("{0} is {1} year old ".format(name,age))


answer=5
guess=int(input("enter your guess :"))
#while True:
if guess>answer:
        print("enter smaller value: ", )
        guess = int(input(" try agian :"))
        if guess==answer:
           print("guess is correct")
        else:
            print("guess is incorrect sorry")
elif guess<answer:
        print("enter higher value: ")
        guess = int(input(" try agian :"))
        if guess==answer:
           print("guess is correct")
        else:
            print("guess is incorrect sorry")
else:
        print("guess is correct")

name=input("Please enter your name :")
age=int(input("Hi! {0} please enter your age :".format(name)))

if 18<age<31:
    print("Welcome to the group 18-31 holiday!")
elif 31<age<18:
    print("We apologies our policies suggest us not to allow you in the holiday")
else:
    print("Please check the input values")
