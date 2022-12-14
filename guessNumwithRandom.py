import random
lower=5
higher=10

while True:

    guess = int(input("please enter the guess, choose value between {} and {}:".format(lower, higher)))
    answer = random.randint(lower, higher)
    if guess>answer:
        st='lower'
    else:st='higher'

    if guess==answer:
        print("congratulations, you guess it right")
        break

    else:
        print("please retry : correct answer is {}, enter {} value".format(answer,st))
    choice=input("Press Y to continue :")
    if choice=='y'.casefold():
        continue
    else:break
        # guess=int(input("please enter the guess, choose value between {} and {}:".format(lower,higher)))


