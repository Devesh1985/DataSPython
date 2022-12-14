string=input("enter your string :\n")
for i in string:
    if i.isalnum()==False:
     continue
    print(True)
    break
else:print(False)
for i in string:
    if  i.isalpha()==False:
     continue
    print(True)
    break
else:print(False)
for i in string:
    if i.isdigit()==False:
     continue
    print(True)
    break
else:
    print(False)
for i in string:
    if i.islower()==False:
      continue
    print(True)
    break
else:
    print(False)
for i in string:
    if i.isupper()==False:
     continue
    print(True)
    break
else:
     print(False)


