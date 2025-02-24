"""
------------------------------------------------------------------------
Assignment 9, task 1
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import file_top

fh = open("students.txt","r",encoding="utf-8")

print(f"{file_top(fh, 3)}")

fh.close()