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


guess_1 = input("Guess a letter: ")

word_status = "________"

if len(guess_1) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_1 == "a":
            word_status_list1 = list(word_status)
            word_status_list1[0] = guess_1
            word_status_list1[1] = guess_1
            word_status_list1[5] = guess_1
            word_status_g1 = "".join(word_status_list1)
            word_status = word_status_g1
            print(f"""{word_status_g1}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_1 == "r":
            word_status_list1 = list(word_status)
            word_status_list1[2] = guess_1
            word_status_list1[6] = guess_1
            word_status_g1 = "".join(word_status_list1)
            word_status = word_status_g1
            print(f"""{word_status_g1}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_1 == "d":
            word_status_list1 = list(word_status)
            word_status_list1[3] = guess_1
            word_status_g1 = "".join(word_status_list1)
            word_status = word_status_g1
            print(f"""{word_status_g1}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_1 == "v":
            word_status_list1 = list(word_status)
            word_status_list1[4] = guess_1
            word_status_g1 = "".join(word_status_list1)
            word_status = word_status_g1
            print(f"""{word_status_g1}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_1 == "k":
            word_status_list1 = list(word_status)
            word_status_list1[7] = guess_1
            word_status_g1 = "".join(word_status_list1)
            word_status = word_status_g1
            print(f"""{word_status_g1}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    attempts -= 1


guess_2 = input("Guess a letter: ")

if len(guess_2) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_2 == "a":
            word_status_list2 = list(word_status)
            word_status_list2[0] = guess_2
            word_status_list2[1] = guess_2
            word_status_list2[5] = guess_2
            word_status_g2 = "".join(word_status_list2)
            word_status = word_status_g2
            print(f"""{word_status_g2}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_2 == "r":
            word_status_list2 = list(word_status)
            word_status_list2[2] = guess_2
            word_status_list2[6] = guess_2
            word_status_g2 = "".join(word_status_list2)
            word_status = word_status_g2
            print(f"""{word_status_g2}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_2 == "d":
            word_status_list2 = list(word_status)
            word_status_list2[3] = guess_2
            word_status_g2 = "".join(word_status_list2)
            word_status = word_status_g2
            print(f"""{word_status_g2}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_2 == "v":
            word_status_list2 = list(word_status)
            word_status_list2[4] = guess_2
            word_status_g2 = "".join(word_status_list2)
            word_status = word_status_g2
            print(f"""{word_status_g2}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_2 == "k":
            word_status_list2 = list(word_status)
            word_status_list2[7] = guess_2
            word_status_g2 = "".join(word_status_list2)
            word_status = word_status_g2
            print(f"""{word_status_g2}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    attempts -= 1


guess_3 = input("Guess a letter: ")

if len(guess_3) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_3 == "a":
            word_status_list3 = list(word_status)
            word_status_list3[0] = guess_3
            word_status_list3[1] = guess_3
            word_status_list3[5] = guess_3
            word_status_g3 = "".join(word_status_list3)
            word_status = word_status_g3
            print(f"""{word_status_g3}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_3 == "r":
            word_status_list3 = list(word_status)
            word_status_list3[2] = guess_3
            word_status_list3[6] = guess_3
            word_status_g3 = "".join(word_status_list3)
            word_status = word_status_g3
            print(f"""{word_status_g3}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_3 == "d":
            word_status_list3 = list(word_status)
            word_status_list3[3] = guess_3
            word_status_g3 = "".join(word_status_list3)
            word_status = word_status_g3
            print(f"""{word_status_g3}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_3 == "v":
            word_status_list3 = list(word_status)
            word_status_list3[4] = guess_3
            word_status_g3 = "".join(word_status_list3)
            word_status = word_status_g3
            print(f"""{word_status_g3}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_3 == "k":
            word_status_list3 = list(word_status)
            word_status_list3[7] = guess_3
            word_status_g3 = "".join(word_status_list3)
            word_status = word_status_g3
            print(f"""{word_status_g3}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    attempts -= 1


guess_4 = input("Guess a letter: ")

if len(guess_4) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_4 == "a":
            word_status_list4 = list(word_status)
            word_status_list4[0] = guess_4
            word_status_list4[1] = guess_4
            word_status_list4[5] = guess_4
            word_status_g4 = "".join(word_status_list4)
            word_status = word_status_g4
            print(f"""{word_status_g4}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_4 == "r":
            word_status_list4 = list(word_status)
            word_status_list4[2] = guess_4
            word_status_list4[6] = guess_4
            word_status_g4 = "".join(word_status_list4)
            word_status = word_status_g4
            print(f"""{word_status_g4}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_4 == "d":
            word_status_list4 = list(word_status)
            word_status_list4[3] = guess_4
            word_status_g4 = "".join(word_status_list4)
            word_status = word_status_g4
            print(f"""{word_status_g4}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_4 == "v":
            word_status_list4 = list(word_status)
            word_status_list4[4] = guess_4
            word_status_g4 = "".join(word_status_list4)
            word_status = word_status_g4
            print(f"""{word_status_g4}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_4 == "k":
            word_status_list4 = list(word_status)
            word_status_list4[7] = guess_4
            word_status_g4 = "".join(word_status_list4)
            word_status = word_status_g4
            print(f"""{word_status_g4}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    attempts -= 1


guess_5 = input("Guess a letter: ")

if len(guess_5) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_5 == "a":
            word_status_list5 = list(word_status)
            word_status_list5[0] = guess_5
            word_status_list5[1] = guess_5
            word_status_list5[5] = guess_5
            word_status_g5 = "".join(word_status_list5)
            word_status = word_status_g5
            print(f"""{word_status_g5}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_5 == "r":
            word_status_list5 = list(word_status)
            word_status_list5[2] = guess_5
            word_status_list5[6] = guess_5
            word_status_g5 = "".join(word_status_list5)
            word_status = word_status_g5
            print(f"""{word_status_g5}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_5 == "d":
            word_status_list5 = list(word_status)
            word_status_list5[3] = guess_5
            word_status_g5 = "".join(word_status_list5)
            word_status = word_status_g5
            print(f"""{word_status_g5}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_5 == "v":
            word_status_list5 = list(word_status)
            word_status_list5[4] = guess_5
            word_status_g5 = "".join(word_status_list5)
            word_status = word_status_g5
            print(f"""{word_status_g5}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_5 == "k":
            word_status_list5 = list(word_status)
            word_status_list5[7] = guess_5
            word_status_g5 = "".join(word_status_list5)
            word_status = word_status_g5
            print(f"""{word_status_g5}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    if word_status == word:
        print(f"""Congratulations! You win!
The word was {word}!""")
        quit()
    attempts -= 1


guess_6 = input("Guess a letter: ")

if len(guess_6) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_6 == "a":
            word_status_list6 = list(word_status)
            word_status_list6[0] = guess_6
            word_status_list6[1] = guess_6
            word_status_list6[5] = guess_6
            word_status_g6 = "".join(word_status_list6)
            word_status = word_status_g6
            print(f"""{word_status_g6}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_6 == "r":
            word_status_list6 = list(word_status)
            word_status_list6[2] = guess_6
            word_status_list6[6] = guess_6
            word_status_g6 = "".join(word_status_list6)
            word_status = word_status_g6
            print(f"""{word_status_g6}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_6 == "d":
            word_status_list6 = list(word_status)
            word_status_list6[3] = guess_6
            word_status_g6 = "".join(word_status_list6)
            word_status = word_status_g6
            print(f"""{word_status_g6}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_6 == "v":
            word_status_list6 = list(word_status)
            word_status_list6[4] = guess_6
            word_status_g6 = "".join(word_status_list6)
            word_status = word_status_g6
            print(f"""{word_status_g6}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_6 == "k":
            word_status_list6 = list(word_status)
            word_status_list6[7] = guess_6
            word_status_g6 = "".join(word_status_list6)
            word_status = word_status_g6
            print(f"""{word_status_g6}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    if word_status == word:
        print(f"""Congratulations! You win!
The word was {word}!""")
        quit()
    attempts -= 1


guess_7 = input("Guess a letter: ")

if len(guess_7) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_7 == "a":
            word_status_list7 = list(word_status)
            word_status_list7[0] = guess_7
            word_status_list7[1] = guess_7
            word_status_list7[5] = guess_7
            word_status_g7 = "".join(word_status_list7)
            word_status = word_status_g7
            print(f"""{word_status_g7}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_7 == "r":
            word_status_list7 = list(word_status)
            word_status_list7[2] = guess_7
            word_status_list7[6] = guess_7
            word_status_g7 = "".join(word_status_list7)
            word_status = word_status_g7
            print(f"""{word_status_g7}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_7 == "d":
            word_status_list7 = list(word_status)
            word_status_list7[3] = guess_7
            word_status_g7 = "".join(word_status_list7)
            word_status = word_status_g7
            print(f"""{word_status_g7}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_7 == "v":
            word_status_list7 = list(word_status)
            word_status_list7[4] = guess_7
            word_status_g7 = "".join(word_status_list7)
            word_status = word_status_g7
            print(f"""{word_status_g7}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_7 == "k":
            word_status_list7 = list(word_status)
            word_status_list7[7] = guess_7
            word_status_g7 = "".join(word_status_list7)
            word_status = word_status_g7
            print(f"""{word_status_g7}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    if word_status == word:
        print(f"""Congratulations! You win!
The word was {word}!""")
        quit()
    attempts -= 1


guess_8 = input("Guess a letter: ")

if len(guess_8) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_8 == "a":
            word_status_list8 = list(word_status)
            word_status_list8[0] = guess_8
            word_status_list8[1] = guess_8
            word_status_list8[5] = guess_8
            word_status_g8 = "".join(word_status_list8)
            word_status = word_status_g8
            print(f"""{word_status_g8}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_8 == "r":
            word_status_list8 = list(word_status)
            word_status_list8[2] = guess_8
            word_status_list8[6] = guess_8
            word_status_g8 = "".join(word_status_list8)
            word_status = word_status_g8
            print(f"""{word_status_g8}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_8 == "d":
            word_status_list8 = list(word_status)
            word_status_list8[3] = guess_8
            word_status_g8 = "".join(word_status_list8)
            word_status = word_status_g8
            print(f"""{word_status_g8}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_8 == "v":
            word_status_list8 = list(word_status)
            word_status_list8[4] = guess_8
            word_status_g8 = "".join(word_status_list8)
            word_status = word_status_g8
            print(f"""{word_status_g8}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_8 == "k":
            word_status_list8 = list(word_status)
            word_status_list8[7] = guess_8
            word_status_g8 = "".join(word_status_list8)
            word_status = word_status_g8
            print(f"""{word_status_g8}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    if word_status == word:
        print(f"""Congratulations! You win!
The word was {word}!""")
        quit()
    attempts -= 1


guess_9 = input("Guess a letter: ")

if len(guess_9) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_9 == "a":
            word_status_list9 = list(word_status)
            word_status_list9[0] = guess_9
            word_status_list9[1] = guess_9
            word_status_list9[5] = guess_9
            word_status_g9 = "".join(word_status_list9)
            word_status = word_status_g9
            print(f"""{word_status_g9}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_9 == "r":
            word_status_list9 = list(word_status)
            word_status_list9[2] = guess_9
            word_status_g9 = "".join(word_status_list9)
            word_status = word_status_g9
            print(f"""{word_status_g9}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_9 == "d":
            word_status_list9 = list(word_status)
            word_status_list9[3] = guess_9
            word_status_g9 = "".join(word_status_list9)
            word_status = word_status_g9
            print(f"""{word_status_g9}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_9 == "v":
            word_status_list9 = list(word_status)
            word_status_list9[4] = guess_9
            word_status_g9 = "".join(word_status_list9)
            word_status = word_status_g9
            print(f"""{word_status_g9}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_9 == "k":
            word_status_list9 = list(word_status)
            word_status_list9[7] = guess_9
            word_status_g9 = "".join(word_status_list9)
            word_status = word_status_g9
            print(f"""{word_status_g9}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    if word_status == word:
        print(f"""Congratulations! You win!
The word was {word}!""")
        quit()
    attempts -= 1


guess_10 = input("Guess a letter: ")

if len(guess_10) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_10 == "a":
            word_status_list10 = list(word_status)
            word_status_list10[0] = guess_10
            word_status_list10[1] = guess_10
            word_status_list10[5] = guess_10
            word_status_g10 = "".join(word_status_list10)
            word_status = word_status_g10
            print(f"""{word_status_g10}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_10 == "r":
            word_status_list10 = list(word_status)
            word_status_list10[2] = guess_10
            word_status_g10 = "".join(word_status_list10)
            word_status = word_status_g10
            print(f"""{word_status_g10}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_10 == "d":
            word_status_list10 = list(word_status)
            word_status_list10[3] = guess_10
            word_status_g10 = "".join(word_status_list10)
            word_status = word_status_g10
            print(f"""{word_status_g10}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_10 == "v":
            word_status_list10 = list(word_status)
            word_status_list10[4] = guess_10
            word_status_g10 = "".join(word_status_list10)
            word_status = word_status_g10
            print(f"""{word_status_g10}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_10 == "k":
            word_status_list10 = list(word_status)
            word_status_list10[7] = guess_10
            word_status_g10 = "".join(word_status_list10)
            word_status = word_status_g10
            print(f"""{word_status_g10}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    if word_status == word:
        print(f"""Congratulations! You win!
The word was {word}!""")
        quit()
    attempts -= 1


guess_11 = input("Guess a letter: ")

if len(guess_11) > 1:
    print("Please only guess one letter at a time.")
else:
    while attempts > 0:
        if guess_11 == "a":
            word_status_list11 = list(word_status)
            word_status_list11[0] = guess_11
            word_status_list11[1] = guess_11
            word_status_list11[5] = guess_11
            word_status_g11 = "".join(word_status_list11)
            word_status = word_status_g11
            print(f"""{word_status_g11}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_11 == "r":
            word_status_list11 = list(word_status)
            word_status_list11[2] = guess_11
            word_status_g11 = "".join(word_status_list11)
            word_status = word_status_g11
            print(f"""{word_status_g11}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_11 == "d":
            word_status_list11 = list(word_status)
            word_status_list11[3] = guess_11
            word_status_g11 = "".join(word_status_list11)
            word_status = word_status_g11
            print(f"""{word_status_g11}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_11 == "v":
            word_status_list11 = list(word_status)
            word_status_list11[4] = guess_11
            word_status_g11 = "".join(word_status_list11)
            word_status = word_status_g11
            print(f"""{word_status_g11}
You have {attempts - 1} guesses remaining.""")
            break
        elif guess_11 == "k":
            word_status_list11 = list(word_status)
            word_status_list11[7] = guess_11
            word_status_g11 = "".join(word_status_list11)
            word_status = word_status_g11
            print(f"""{word_status_g11}
You have {attempts - 1} guesses remaining.""")
            break
        else:
            print(f"Nope! Try again! You have {attempts - 1} guesses remaining.")
            break
    if word_status == word:
        print(f"""Congratulations! You win!
The word was {word}!""")
        quit()
    else:
        print("Sorry! You're out of turns. You lose :'(")
        quit()