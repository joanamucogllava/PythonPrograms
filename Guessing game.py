#This pogram will ask you to guess the secret word in 3 times. If you find it,
#you win and if you don't or you run out of guesses you lose.
# Author: Joana Mucogllava

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("YOU WIN!")
