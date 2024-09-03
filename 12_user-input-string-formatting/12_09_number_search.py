# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number = int(input("Please enter a number between 0 and 1,000,000,000: "))

if number < 0 or number > 1000000000:
    print("Error. The number entered must be between 0 and 1,000,000,000.")
else:
    n = 0
    while n != number:
        n += 1
    print(n)
    