# This program will ask the user to enter a word and after reversing it, it will determine if the word is palindrome or not.
# Author: Joana Mucogllava

wrd = input ("Please enter a word: ")
word = str(wrd)
rvs = wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This is a palindorome.")
else:
    print("This word is not palindrome.")
