lst=["milk","pasta","spam","vegetables","chees","oil"]
for items in lst:
    if items=="spam":
        continue

    print(items)

lst=["milk","pasta","spam","vegetables","chees","oil"]
found_at=None
item_to_find="sam"
# for index in range(len(lst)):
#     if lst[index]==item_to_find:
#         found_at=index
#         break
if item_to_find in lst:
    found_at=lst.index(item_to_find)
if found_at==None:
    print("{} not found".format(item_to_find))
else:
    print("the {0} is in index {1} ".format(item_to_find,found_at))

