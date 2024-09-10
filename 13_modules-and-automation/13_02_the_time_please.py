# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

import datetime

now = datetime.datetime.now()

print("now =", now)


date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

print(date_time)