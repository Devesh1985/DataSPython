string='abcdefghijklmnopqrstuvwxyz'
width=4

# def wrap(string,width):
#     res=" "
#     for i in range(0,len(string),width):
#        res+=string[i:i+width]
#
# print(wrap(string,width))

def wrap(string,width):
    res=""
    for i in range(0,len(string),width):
        res = res+string[i:i+width]+"\n"
    return res

print(wrap(string,width))