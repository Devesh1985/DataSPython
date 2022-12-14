print("there are {0} day in {1} {2} {3} {4} {5} {6}".format(31,'jan','mar','april','may','jun','july'))

print("""there are {0} day in {1} {2} {3} {4} {5} {6}
""".format(31,'jan','mar','april','may',    'jun','july'))

for i in range(1,13):
    print("the {0:2} square is {1:3} and cube is {2:4}".format(i,i*i,i*i*i))


pi=22/7
print(pi)
print("{0:12f}".format(22/7))


#fstring
print(f"{22/7} is pi value")

age=99
#print("he is"+ {age}+" year old can not workout")
print(f"he is {age} year old,he can not workout")
#print(f and thn the block to execute)

print(f"pi value is {22/7:.02f}")