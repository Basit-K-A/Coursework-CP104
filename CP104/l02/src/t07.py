"""
------------------------------------------------------------------------
Lab 2, task 7
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""

numFlyers = int(input("Number of flyers: "))
numVolunteers = int(input("Number of volunteers: "))

flyersPer = int(numFlyers//numVolunteers)
flyersLeft = int((numFlyers%numVolunteers))

print(f"Flyers per volunteer: {flyersPer}")
print(f"Flyers left over: {flyersLeft}")

