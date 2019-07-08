# This program will show the provided birthdays and you will pick up which one you want to look for.


import time
Birthday = {
    "Utku Yurter": "03/17/1998",
    "Joana Mucogllava": "07/31/1997",
    "Fiqiri Mucogllava": "01/01/1968",
}
print("Welcome to the Birthday game! We have the birthdays to:")
time.sleep(1)
for x in Birthday:
    print(x)
    time.sleep(0.7)
choice = input("\nWho's birthday do you want to look up?")

if choice in Birthday:
    print("The birthday of {} is: ".format(choice))
    print(Birthday[choice])
