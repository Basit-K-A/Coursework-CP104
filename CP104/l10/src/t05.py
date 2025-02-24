"""
------------------------------------------------------------------------
Lab 10, task 5
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import customer_append

fh = open('customers.txt','r+',encoding='utf-8')

print(f"{customer_append(fh,['35612', 'David', 'Brown', 237.56, '2008-10-10'])}")