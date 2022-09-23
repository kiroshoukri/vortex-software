secret_word = "duno"
guess = ""
guess_count = 0
guess_limit = 3

while guess_count < guess_limit and secret_word != guess:
    guess = input("enter guess word: ")
    guess_count +=1
if (secret_word == guess):
    print("you win!")
else:
    print("out of guesses, you lose!")