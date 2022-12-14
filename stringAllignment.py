def allign(n):
    string='D'
    for i in range(n):
        print((string*i).rjust(n,'-')+string+string*i)

    for i in range(n):
        print((string*(n-2)).rjust(n,'-')+string+string*(n-2))

    for i in range(n//2):
        print((string*(n*5)).rjust((n+22),'-'))

    #print(string.ljust(3,'-'))
    #print(string.rjust(4,'-'))


allign(int(input()))