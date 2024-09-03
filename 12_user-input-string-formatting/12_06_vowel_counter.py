# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

phrase = input("Type any phrase: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

count = 0

for char in phrase:
    if char in vowels:
        count += 1

print(f"There are {count} vowels in the phrase '{phrase}'.")
