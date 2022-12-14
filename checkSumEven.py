def sum_eo(n, t):
    """
    This will calculate the sum of the given 'n' natural even or odd numbers
    based on the value of parameter 't'
    :param n: provide range for the sequence
    :param t: specify even or odd
    :return: sum of the sequence
    """
    res=0
    if t == 'e':
        for i in range(2, n, 2):
            print(i)
            res += i
        return res
    elif t == 'o':
        for i in range(1, n, 2):
            res += i
        return res
    else:
        return -1

print(sum_eo(10,'e'))




def if_armstrong(num):
    """
    Functions checks if the given number is armstrong or not
    :param num: to be checked if armstrong or not
    :return: None
    """
    n=str(num)
    cube=0
    for i in n:
        cube=cube+int(i)**3
    if cube==num:
        print(True)
    else:
        print(False)

if_armstrong(153)


def count_Str(string):
    """
    function count the occurrence of the character in the string
    :param string: where we need to check char occurrence
    :return: None
    """
    count=0
    for i in string:
        ch=i
        if ch==i:
            count += 1
            print(ch,count)
        else:
            #ch="-"
            count=0



count_Str("ttyyhello")

def fib_again(n):
    """
    Fucntion prints fibonacci series till a given no
    :param n: range to print the fibonacci series for
    :return: None
    """
    a=0
    b=1
    #c=a+b
    print("fibonacci starts from here:\n",a,"\n",b)
    for i in range(n):
        c = a + b
        a = b
        b = c


        print(c)

fib_again(30)

