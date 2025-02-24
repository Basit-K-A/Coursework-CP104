"""
------------------------------------------------------------------------
Lab 2, task 1
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-18"
------------------------------------------------------------------------
"""
FAHRENHEIT_FREEZING = 32

celsius = int(input("Temperature (C): "))

fah = str(((9/5)*celsius + FAHRENHEIT_FREEZING))

print(f"Temperature (F): {fah}")
