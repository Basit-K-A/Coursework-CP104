"""
------------------------------------------------------------------------
Assignment 1, task 1
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-03"
------------------------------------------------------------------------
"""

TAX_RATE = 18.50

sales = float(input("Total sales: $ "))

taxed = (TAX_RATE/100)*sales

print(f"""
Projected Tax Report
----------------------
Total sales: $ {sales:.2f}

Annual tax:  % {TAX_RATE:.2f}
----------------------
Tax:         $ {taxed:.2f}
""")