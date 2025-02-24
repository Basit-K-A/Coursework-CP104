"""
------------------------------------------------------------------------
Lab 2, task 6
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-20"
------------------------------------------------------------------------
"""

mPrincipal = float(input("Mortgage principal ($): "))
numYears = float(input("Number of years:"))
interestRate = int(input("Yearly interest rate (%): "))

monthlyRate = (interestRate/12)/100
numPayments = numYears*12

numerator = monthlyRate*((1 + monthlyRate)**numPayments)
denominator = ((1 + monthlyRate)**numPayments)-1

monthPayments = (mPrincipal*(numerator/denominator))
roundedTotal = ("%.2f" % monthPayments)

print(f"The monthly payments are; ${roundedTotal}")