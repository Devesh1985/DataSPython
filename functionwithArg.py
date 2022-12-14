# defaul argumnent

def calc(x,y,op):
    if op =='+':
        return (x+y)
    elif op=='-':
        return (x-y)
    elif op=='*':
        return (x*y)
    else:
        return ("Please enter correct operator :",)

#print(calc(4,8,''))

def minion_game(string):
    ls=""
    con=""
    #for i in string:
    #ls=string.split()[:2]
    i=1
    #for i in range(len(string)):

    while i<len(string):
        #if string[i] in ('a','e')
        print(string[0:i])
        print(string[1:i+1])
        print(string[2:i+2])
        print(string[3:i+3])
        i+=1


#         if i.casefold() in ('a','e','i','o','u'):
#             ls=ls+i
#         else:
#             con=con+i
#     for j in string:
#
#     print(ls,"this is con :",con)
#
minion_game('BANANA')
