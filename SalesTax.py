# This program will show the amount of the tax
# you will be charged based on the purchase amount.

purchaseAmount = eval(input("Enter purchase amount: "))
tax = purchaseAmount * 0.0825
print("Sales tax is", int(tax * 100) / 100.0)
