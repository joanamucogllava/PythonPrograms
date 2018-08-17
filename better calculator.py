# This program will ask the user to enter 2 numberes and the operator that he wants to use.

num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
