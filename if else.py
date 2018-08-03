# Author: Joana Mucogllava
a = 'y'
while(a == 'y' or a == 'Y'):
    

    print("Enter a number: ")
    n = int(input())


    if(n%2 != 0):
        print ("Weird")
    elif (n%2 == 0):
        if(n >= 2 and n <= 5):
            print ("Not Weird")
        elif(n >= 6 and n <= 20):
            print("Weird")
        elif(n > 20):
            print("Not Weird")

    print("Do you want to continue? \n Enter y or n: ")
    a = input()
    
print("Thank You!")
