#take input from user

dictUser={"mutable":"which we can change","set":"collection of different data type, that contains unique values"
    ,"python":"is a general purpose programming language","abondaon":"to leave someone/something"}
word=input("enter the word :")
print("meaning of the word is :",dictUser[word])


"""age=int(input("Please tell us your age, age must be between 7-99 :"))
if age>99 or age<7:
    print("please enter the age between 7-99")
elif age>18:
    print("You are above 18, you can drive")
elif age<18:
    print("you are below 18, please read instruction carefully and do not drive till you cross 18")
elif age==18:
    print("we cant decide if you can drive or not, you will have to come to RTO directly")
"""