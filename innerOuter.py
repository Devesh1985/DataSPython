def outer(a,b):
    #return a*b

    def add(a,b):
        return a+b
    return add(a,b)




fun=outer(10,23)
print(fun)
