"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import file_statistics

file_handle = open("addresses.txt","r",encoding="utf-8")

print(f"{file_statistics(file_handle)}")

file_handle.close()