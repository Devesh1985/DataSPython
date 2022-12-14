def student(name,age):
    print(name,age)


student('nina',89)
student(age=23,name='raja')
# student()

def stud(*name,**age):
    print(name,age)

# stud('ram','shyam','gopal',age=22,33,44,55)