"""
------------------------------------------------------------------------
Lab 2, task 10
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-20"
------------------------------------------------------------------------
"""

foodCost = float(input("Food Charge: $"))
sTax = float(input("Sales Tax in (%): "))
tipPercent = float(input("Tip in (%): "))

taxTotal = foodCost*(sTax/100)
tipTotal = foodCost*(tipPercent/100)
foodTotal = foodCost+taxTotal+tipTotal

print(f"Subtotal: $ {foodCost}")

print(f"Tax: $ {taxTotal}")

print(f"Tip: $ {tipTotal}")

print(f"Total: $ {foodTotal}")