# op_1="Learn Python"
# op_2="Learn Java"
# op_3="Learn behavioural skills"
# op_4="Learn photography"
# op_5="Exit"
#
# option=int(input("Please select\n1: for {}\n2: for {}\n3: for {}\n4: for {}\n5: to {}\n".format(op_1,op_2,op_3,op_4,op_5)))
# while True:
#     if option==1:
#         print("Great you have chosen to {}".format(op_1))
#         break
#     elif option==2:
#         print("Great you have chosen to {}".format(op_2))
#         break
#     elif option ==3:
#         print("Great you have chosen to {}".format(op_3))
#         break
#     elif option ==4:
#         print("Great you have chosen to {}".format(op_4))
#         break
#     elif option==0:
#         print("Great you have chosen to {}".format(op_5))
#         break
# else:
#     print("You have choosen:",option)

# same thing in different way


choice="-"
wish="-"
while True:

    if choice==5:
        break
    elif choice in (1,2,3,4):
        print("you have chosen {},try again with a value in 1-4".format(choice))

    else:
        print("1\t:Learn Python")
        print("2\t:Learn Java")
        print("3\t:Learn behavioural skills")
        print("4\t:Learn photography")
        print("5\t:Exit")
    choice = int(input())
