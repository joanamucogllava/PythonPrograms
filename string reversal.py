wrd = input ("Please enter a word: ")
word = str(wrd)
rvs = wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This is a palindorome.")
else:
    print("This word is not palindrome.")
