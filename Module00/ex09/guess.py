import sys
from random import randint

print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")

douglas_adams = "The answer to the ultimate question of life, \
the universe and everything is 42."

solution = randint(1, 99)
guess = 0
attemps = 0

while guess != solution:
    attemps += 1
    str_guess = input("What's your guess between 1 and 99?\n")
    if str_guess == "exit":
        sys.exit("Goodbye!")
    try:
        guess = int(str_guess)
        if guess > solution:
            print("Too high!")
        if guess < solution:
            print("Too low!")
    except ValueError:
        print("That's not a number.")

if (solution == 42):
    print(douglas_adams)

if attemps == 1:
    print("Congratulations! You got it on your first try!")
else:
    print("You won in {0} attemps!".format(attemps))
