#Create a random number guessing game in python

import random

n = random.randint(1,10)

tries = 0

while True:
    guess = int(input("Guess the number:- "))
    if n == guess:
        tries +=1
        print(f"You guessed it right in {tries} tries")
        break
    elif n > guess:
        tries+=1
        print("Go a little higher")
    elif n < guess:
        tries+=1
        print("Go a little lower")
    else:
        tries+=1
        print("you are wrong")
