def check_palindrom(num):
    ls=list(str(num)) # below code is also correct but optimized
    # if ls==ls[::-1]:
    #     print(True)
    # else:
    #     print(False)
    #print(ls[::-1])
    return ls==ls[::-1]



for i in list([233,44,5432,98898,7878,7667,541541]):
    res=check_palindrom(i)
    print(res)
    break



def check_pal_str(string):
    print(string.casefold())
    print(string[::-1])
    return string.casefold()==string[::-1].casefold()




print("this will print string output :",check_pal_str("Ratdar"))



def pal_sentance(sntnce):
    ls=""
    sntnce=list(sntnce)
    for i in sntnce:
        if i.isalpha():
            ls=ls+i
    print("checcking the flow",ls)
    return ls.casefold()==ls[::-1].casefold()

print(pal_sentance("Mr. Owl ate my metal worm"))
print(pal_sentance("Was it a car, or a cat, I saw?"))
print(pal_sentance("Do geese see god?"))






