# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

word_one = input("Please provide word number 1: ")
word_two = input("Please provide word number 2: ")
word_three = input("Please provide word number 2: ")

longest = max(word_one, word_two, word_three, key = len)

print(f"{len(longest)}, {longest}")