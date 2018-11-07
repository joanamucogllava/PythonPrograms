# This program will ask you to guess a number up to 100 until you find it.

import random

number = random.randint(0, 100)

print("Guess a magic number between 0 and 100")

guess = -1
while guess != number:
    guess = eval(input("Enter your guess: "))

    if guess == number:
        print("Yes, the number is", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

    
