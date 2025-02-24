"""
------------------------------------------------------------------------
Assignment 2, task 3
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-03"
------------------------------------------------------------------------
"""

unformDate = int(input("Enter a date in the format YYYYMMDD: "))

day = unformDate%100

month = (unformDate//100)%100

year = (unformDate//10000)

print(f"The reformatted date: {year}/{month:02d}/{day:02d}")