# This program will raise the given base number to the given power number and print out the result.
# Author: Joana Mucogllava

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))
