# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

word = "aardvark"


word_len = len(word)

print(f"Let's play Hangman! You have 11 guesses to solve the {word_len} letter word!")

print("_ " * word_len + "\n")

attempts = 11

aardvark = "________"

while attempts > 0:
    guess = input("Guess a letter: ")
    if len(guess) > 1:
        print("Please only guess one letter at a time.")
    elif guess in word:
        hangman = list(aardvark)
        for i, letter in enumerate(word):
            if letter == guess:
                hangman[i] = guess
        aardvark = "".join(hangman)
        if "_" not in aardvark:
            print(f"""{aardvark}
Congratulations! You win! The word was {word}.""")
            quit()
        else:
            print(f"""{aardvark}
You have {attempts - 1} guesses remaining.""")
    else:
        print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
    attempts -= 1

if attempts == 0:
    print(f"Sorry! You're out of turns. You lose :'(. The word was {word}.")
    quit()