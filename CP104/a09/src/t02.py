"""
------------------------------------------------------------------------
Assignment 9, task 2
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import read_integers

fh = open("numbers.txt","r",encoding="utf-8")

print(f"{read_integers(fh)}")

fh.close()