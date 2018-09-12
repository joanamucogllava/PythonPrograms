# This program is going to ask the user to guess a random number
# between 0 and 100 until they find the secret number.
# Author: Joana Mucogllava

import random
number = random.randint(0, 100)
guesses = 0

while 1:
    guess = int(input("Enter an integer from 0 to 100: "))
    guesses += 1
    print ("This is your %d guess" %guesses)

    if guess < number:
        print("Your guess is low!")
    elif guess > number:
        print("Your guess is high!")
    elif guess == number:
        break
    
if guess == number:
    guesses = str(guesses)
    print("You guess it in :", guesses + " guesses")

else:
    number = str(number)
    print("The secret number was ", number)
