#Function: fuction is a block of code, that returns some specific task and can take some parameter
# from outside to perform specific tasks
#In python we define/create function by using def keyword, so the syntax of a function
# def functionName(arguments):
      #function body OR tasks
      #return VALUE
# to call the same function
# functionName(prameter)

def zipFunction(listA,listB):
    dicta={}
    #listA=listA
    #listB=listB
    for i,j in zip(listA,listB):
        #print(index,i)
        dicta[i]=j
        return dicta
    print(dicta)

zipFunction([3,5,6,9,10,11],["wifi","broadband","alone","happening"])

# a simple python function to check if passed number is even or Odd
userInput=input("type 'y' if you want to start \n")
while userInput=='y':
    num=int(input("enter num :\n"))
    if num%2==0:
        print(f"{num} is even")
        userInput=input("type 'y' agar fir try karna hai to ? :\n")
    elif num==0:
        userInput=input("invalid input enter value > 0, type 'y' agar fir se try karna hai to? \n")
    else:
        print(f"{num} is odd")
        userInput=input("type 'y' agar fir try karna hai to ? :\n")






