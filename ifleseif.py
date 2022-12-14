import time

userwant='yes'
num = int(input("enter your choice :\n"))
while userwant=='yes':
    if num==1:
        print("monday")
    elif num==2:
        print("tuesday")
    elif num==3:
        print("wednesday")
    elif num == 4:
        print("thuresday")
    elif num == 5:
        print("friday")
    elif num == 6:
        print("saturday")
    elif num==7:
        print("sunday")
    else: print("enter num between 1-7")
    time.sleep(2)
    userwant=input("you want to try again :\n")


