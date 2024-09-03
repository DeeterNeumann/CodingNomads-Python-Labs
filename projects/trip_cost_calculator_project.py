# Receive the following arguments from the user:

# Kilometers to drive
# Liters-per-kilometer usage of the car
# Price per liter of fuel
# Calculate the cost of the trip and display it to the user in the console. \
# Apply some of the string formatting tricks that you learned about in this course section.

distance = int(input("How many kilometers do you plan to drive?: "))
lpk = int(input("How many liters-per-kilometer does the car get that you plan on taking on the drive?: "))
price = float(input("What is the current cost of fuel (per liter)?: "))

trip_cost = ((distance / lpk) * price)

print(f"""The cost to drive {distance} kilometers in a car that gets {lpk} 
liters-per-kilometer at a cost of ${price:.2f} per liter is ${trip_cost:.2f}.""")