string="i am doing revision of python"
string1="I AM DOING REVISION OF PYTHON"
str22="hello123this5is"
dig="121212133"

# capitalize-> will convert sting to sentence case, converting first letter to capital
print(string.capitalize())

#upper-> convert lower to upper case
print(string.upper())

#lower-> convert upper to lower case
print(string1.lower())

#isalnum: if string is numeric
print(string1.isalnum())

# isaplha -> if string is contains alphabets
print(str22.isalpha())

#find-> find particular chr in string, will print the index of the element
print(str22.find('5'))

#isDigit--> return true if string contains all digit
print(dig.isdigit())

#isUpper()/islower() : return true if string contains all caps or all lower

#isprintable()-return if string is printable
ss='99&'
print("this is to check if printable",ss.isprintable())

#isnumeric() will return true if all chr in string are numeric
print(ss.isnumeric())

pi=27/7

print('the value is {:.02f}'.format(pi))
print(f"this value of pi is {pi}")


print("Spock said, \"Live long and prosper.\"")

#help('FORMATTING')




