"""
------------------------------------------------------------------------
Lab 10, task 3
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import customer_best

fh = open('customers.txt','r',encoding='utf-8')

print(f"{customer_best(fh)}")

fh.close()