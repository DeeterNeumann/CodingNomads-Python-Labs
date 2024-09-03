# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

phrase = input("Please type in any phrase: ")
symbol = input("Please enter a symbol: ")

letter = (f"{phrase[0]}")

replaced = phrase.replace(letter, symbol)

print(replaced)

# the tired dog is sleeping throughout the night.

# how would I need to write this code if the first letter of the phrase was capitalized?