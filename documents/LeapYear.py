# This program will ask you 5 times to enter a year 
# and will determine if this year is a Leap year or no.

for i in range(0, 5):

    year = eval(input("Enter a year: "))

    isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
        (year % 400 == 0)

    print(year, "is a leap year?", isLeapYear)
