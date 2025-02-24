"""
------------------------------------------------------------------------
Assignment 2, task 4
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-04"
------------------------------------------------------------------------
"""

flyers = int(input("Number of flyers: "))
delPeeps = int(input("Number of delivery of people: "))

perPeep = flyers//delPeeps
leftOver = flyers%delPeeps

print(f"""
Flyers per delivery person: {perPeep}
Flyers left over: {leftOver}
""")