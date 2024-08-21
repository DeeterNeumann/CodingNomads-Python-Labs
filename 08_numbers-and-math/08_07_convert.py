# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

num = 9
print(type(num))

num = float(num)
print(type(num))

num = int(num)
print(type(num))

quotient = 30.5 / 60
print(quotient)

product = num * quotient
print(product)

float_num = 40.3
float_num_int = int(float_num)
print(float_num_int) #40 Python rounded down

float_num_two = 40.8
float_num_int_two = int(float_num_two)
print(float_num_int_two) #40 Python rounded down despite being closer to 41



