# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

number = random.randint(1, 100)
guess = None

attempts = 10

while guess != number and attempts > 0:
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    else:
        print(f"Nope! Try again! You have {attempts - 1} attempts remaining.")
    attempts -= 1

print(f"The number was {number}.")