"""
------------------------------------------------------------------------
Lab 10, task 12
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import find_shortest

fh = open('words.txt','r',encoding='utf-8')

print(f"{find_shortest(fh)}")

fh.close()