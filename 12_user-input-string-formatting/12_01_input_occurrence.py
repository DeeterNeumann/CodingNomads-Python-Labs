# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

str = input("Please type a phrase: ")
letter = input("Please type any letter found in the phrase you just entered: ")

result = str.index(letter)

print("Result:", result)