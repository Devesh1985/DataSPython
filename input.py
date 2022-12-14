# calc
operation = input("enter the op :")
num1 = int(input("enter the num1 :"))
num2 = int(input("enter the num2 :"))
if operation=="add":
    print(num1+num2)
elif operation=="sub":
    print(num1-num2)
elif operation=="mul":
    print(num1*num2)
elif operation=="div":
    print(num1/num2)
else:
    print("please check your input")
