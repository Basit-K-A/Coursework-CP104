"""
------------------------------------------------------------------------
Assignment 1, task 5
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-11"
------------------------------------------------------------------------
"""

principal = float(input("Principal: "))

interest = float(input("Interest (%): "))

numYears = int(input("Number of years: "))

numInterestPerYear = int(input("Number of times interest compounded per year: "))

intMonth = (interest/100)

parenthesis = 1 + intMonth/numInterestPerYear

exponent = numInterestPerYear*numYears

balance = principal*(parenthesis)**exponent

print(balance)
