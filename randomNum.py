# generate a random number and guess the number from user input
import random
num=int(input("please enter the guess :"))

secretNum=random.randint(2,10)
print("this is randint",secretNum)

scNum1=random.random()
print("this is random:",scNum1)

scnum=random.uniform(2,10)
print("this is uniform :",scnum)

random.seed(10)# base value
print("random with seed",random.randint(10,100))


