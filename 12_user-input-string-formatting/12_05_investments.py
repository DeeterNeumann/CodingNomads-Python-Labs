# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

import math

investment_amount = int(input("How much money are you looking to invest (in dollars)?: "))
interest_rate_percent = int(input("What is the interest rate percent?: "))/100
time = int(input("How many years do you plan to stay in this investment?: "))

fv_eqn = (investment_amount * ((1 + interest_rate_percent)**(time)))

future_value = round(fv_eqn, 2)

print(f"If you invest ${investment_amount} today, in {time} years, your investment will be worth ${future_value}.")
