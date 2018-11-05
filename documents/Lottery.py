# This is a lottery game that will ask you to pick your number 
# and based on your choice you will be consider a winner or a looser. 

import random

lottery = random.randint(0, 99)

guess = eval(input("Enter your lottery pick (two digits): "))

lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigit1 and \
    guessDigit1 == lotteryDigit2):
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1
        or guessDigit1 == lotteryDigit2
        or guessDigit2 == lotteryDigit1
        or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
