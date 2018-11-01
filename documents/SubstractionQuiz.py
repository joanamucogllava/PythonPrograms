# This quiz will test your knowledge in subtracting 2 random numbers between 0 and 100.

import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input("What is "+ str(number1) + " - " +
    str(number2) + "? "))

if number1 - number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", number1, '-',
        number2, "is", number1 - number2, '.')

    
