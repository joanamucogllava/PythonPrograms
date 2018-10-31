for i in range(1, 10):
    number = eval(input("Enter an integer: "))
    if number % 5 == 0:
        print("HiFive")

    if number % 2 == 0:
        print("HiEven")

    if number % 3 == 0:
        print("HiThree")
        
    if number % 5 != 0 and number % 2 != 0 and number % 3 != 0:
        print("Your number is old fashion! :)")
