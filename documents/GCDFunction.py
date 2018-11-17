# This program is finding the GDC of two entered integers by the user. 

def gcd(n1, n2):
    gcd = 1
    k = 2

    while k <= n1 and k <= 2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1

    return gcd


n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest common divisior from", n1,
      "and", n2, "is", gcd(n1, n2))
