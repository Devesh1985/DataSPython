def fib(n):
    """function will take number as a parameter and print the fibonacci series till that range"""

    a,b=0,1
    print('series',a,b,end=" ")
    for i in range(n):
        c=a+b
        #print(34+55,89+55,144+89)
        print(c,end=" ")
        a=b
        b=c


fib(n=int(input()))








