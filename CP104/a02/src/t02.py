"""
------------------------------------------------------------------------
ASsignment 1, task 2
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-03"
------------------------------------------------------------------------
"""

digit = int(input("Enter a positive two digit number: "))

digitTwo = digit//10

digitOne = digit%10

finalDigit = digitTwo-digitOne

print(f"The difference of the digits of {digit} is {finalDigit}")