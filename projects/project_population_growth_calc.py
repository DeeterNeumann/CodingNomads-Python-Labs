# Write the necessary code to display the total population count for the next 3 years (without a leap year).

# Here are the specifications:

# In the country we want to investigate:

# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

current_pop = 380123456
births_per_year = ((1 / 6) * 60 * 24 * 365)
deaths_per_year = ((1 / 12) * 60 * 24 * 365)
immigrants_per_year = ((1 / 40) * 60 * 24 * 365)

pop_year_one = current_pop + births_per_year - deaths_per_year + immigrants_per_year

print("Population Year One:", int(pop_year_one))

pop_year_two = pop_year_one + births_per_year - deaths_per_year + immigrants_per_year

print("Population Year Two:", int(pop_year_two))

pop_year_three = pop_year_two + births_per_year - deaths_per_year + immigrants_per_year

print("Population Year Three:", int(pop_year_three))

