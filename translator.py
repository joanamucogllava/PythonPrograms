# This program will ask the user to enter a phrase and translate it by changing the vowels into "g" letter.
# Author: Joana Mucogllava
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
