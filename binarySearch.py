low=1
max=100
guess=int(input("please think of a number between {} and {}, and press ENTER to continue \n".format(low,max)))

#answer=4
num=low+(max-low)//2
count=1
while num!=guess:
    usrChoice=int(input("This is our attempt no = {}, {} is your number!,\npress 1 if true \nOR press 0 if your number is greater then {},\nelse 2 if what you have in your mind is lower then {}\n ".format(count,num,num,num)))
    if usrChoice==0:
        low=guess+1
        num=low+(max-low)//2
        #count += 1
    elif usrChoice==2:
        max=guess-1
        num=low+(max-low)//2
        #count+=1
    #else:
     #   print("congratulations {} is your no :".format(num))
      #  break
    count+=1
else:
    print("your number is {}".format(num))



