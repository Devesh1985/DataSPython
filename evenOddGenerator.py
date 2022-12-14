def even_odd():

            for n in range(2, 11, 2):
                yield n

            for n in range(1, 11, 2):
                yield n

for i in even_odd():
    print(i)


def fib():
    a,b=0,1
    yield a
    yield b
    while True:
        c=a+b
        yield c
        a,b=b,c

for i in fib():
    if i>26:
        break
    print("fibnacci :",i)