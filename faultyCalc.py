operation = input("enter the operation you want to perform : \n'1: +'\n'2: *'\n'3: /'\n")
num1 = int(input("please enter the num1 : \n"))
num2 = int(input("please enter the num2 : \n"))

#print(num1, num2)

if operation == '*' and (num1 == 45 or num2 == 3):
    print("result is :", 555)
elif operation == '+' and (num1 == 56 or num2 == 9):
        print("result is :",77)
elif operation == '/' and (num1 == 56 or num2 == 6):
        print("result is :",4)
elif operation == '*':
    print(num1*num2)
elif operation=='+':
    print(num1+num2)
elif operation=='/':
    print(num1/num2)
else:
    print("correct your input")








