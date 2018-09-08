# This program will ask the user to insert a number and than it will determine
# whether or not this number is pime.
# Author: Joana Mucogllava

num = int(input("Insert a number: "))
a = [x for x in range(2,num) if num % x == 0]

def is_prime(n):
    if num > 1:
        if len(a) == 0:
            print('prime')
        else:
            print('NOT prime')
    else:
        print('NOT prime')

is_prime(num)
