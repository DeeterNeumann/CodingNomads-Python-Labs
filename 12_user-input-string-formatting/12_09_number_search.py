# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number = int(input("Please enter a number between 0 and 1,000,000,000: "))

n = 0

while n != number:
    n += 1
    break

print(number)

# Need to put upper and lower bound on this code given the range the user was given?