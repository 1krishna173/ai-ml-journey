# Q1
# import math
# print(math.sqrt(25))
# print(math.sin(math.radians(90))

# Alternate

# from math import sqrt,sin,radians
# print(sqrt(25))
# print(sin(radians(90)))

#Q2

# import datetime as d
# print(d.datetime.now())

#Q3 
# from random import randint as r
# print(r(1,100))

# Q4
# from math import sqrt,pow
# print(sqrt(9),pow(2,3))

# try:
#     import non_existent_module
# except ImportError as e:
#     print(f"Error importing module: {e}")

# playing with the operating system os
# import os
# os.mkdir("new.txt") this part creates the file
# os.listdir('.')
# os.rmdir('new.txt')// THis part removes the file
# os.listdir('.')

import datetime

# Current date
today = datetime.date.today()
print(f"Today's date: {today}")

# Date 100 days from today
future_date = today + datetime.timedelta(days=100)
print(f"Date 100 days from today: {future_date}")

# Day of the week for a given date
given_date = datetime.date(2022, 1, 1)
print(f"Day of the week for 2022-01-01: {given_date.strftime('%A')}")

print(datetime.date.today()+datetime.timedelta(days=200))