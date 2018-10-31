# This program will ask you to find the sum of the 2 random numberes from 0 to 9. 

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = eval(input("What is " + str(number1) + " + "
    + str(number2) + "? "))

print(number1, "+", number2, "=", answer,
    "is", number1 + number2 == answer)
