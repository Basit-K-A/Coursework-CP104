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
from functions import append_increment

fh = open('numbers.txt','r+',encoding='utf-8')

print(f"{append_increment(fh)}")

fh.close()