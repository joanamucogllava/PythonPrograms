# This program will ask you to enter integers until your integer is 0
# and will calculate the sum of the entered numbers from you.

data = eval(input("Enter an integer (the input ends " +
    "if it is 0): "))

sum = 0
while data != 0:
    sum += data

    data = eval(input("Enter an integer (the input ends " +
        "if it is 0): "))

print("The sum is", sum)
