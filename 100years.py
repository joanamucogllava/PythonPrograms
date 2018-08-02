#This program will ask for your name and age and will tell you at what age you will turn 100 years old.
name = str(input("What is your name?"))
age = int(input("What is your age?"))
thisyear = int(input("what year is now?"))
year = str((thisyear - age) + 100)
print ("Hello " + name + " you will be 100 years old in the year " + year)
