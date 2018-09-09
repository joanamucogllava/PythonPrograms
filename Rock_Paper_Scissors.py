# In this program a traditional game has been designed, wich will ask 2 different users to introduce their names
# and choose one of the given options in order to see if their selction will win or loose. 
# Any invalid sku entered will be detected by the program and ask the user to try it again.

import sys

user1 = input("What is your name? ")
user2 = input("And your name? ")
user1_answer = input("%s, do you want to choose rock, paper or scissors? " % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors? " % user2)

def compare(u1,u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == "rock":
        if u2 == "scissors":
            return("Rock wins!")
        else:
            return("Paper wins!")
        if u1 == "scissors":
            if u2 == "paper":
                return("Scissors win!")
            else:
                return("Rock wins!")
            if u1 == "paper":
                if u2 == "rock":
                    return("Paper wins!")
                else:
                    return("Scissors win!")
            else:
                return("Invalid input! You have not entered rock, paper or scissors. Please try again!")
                sys.exit()

print(compare(user1_answer, user2_answer))
