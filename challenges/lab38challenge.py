#!/usr/bin/python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def main():

    num = random.randint(1,100)
    rounds = 0
    guess = 0

    while rounds < 5 and guess != num:

        rounds += 1
       
        guess = input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)

        else:
            continue

        if guess > num and rounds <5:
            print("Too high!")

        elif guess < num and rounds <5:
            print("Too low!")

        elif rounds == 5 and guess != num:
            print("Sorry, the answer was " + str(num))

        else:
            print("Correct!")

main()
