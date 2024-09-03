# Use Python's string mini-language to display the table
# that you've built before in a slightly better formatted manner:
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

line_1 = " 0  1  2  3  4  5  6  7  8  9"
line_2 = "10 11 12 13 14 15 16 17 18 19"
line_3 = "20 21 22 23 24 25 26 27 28 29"
line_4 = "30 31 32 33 34 35 36 37 38 39"
line_5 = "40 41 42 43 44 45 46 47 48 49"

table = f"""{line_1}
{line_2}
{line_3}
{line_4}
{line_5}"""

print(table)