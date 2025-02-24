"""
------------------------------------------------------------------------
Lab 10, task 14
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import file_copy_n

filename = "new_words.txt"
fh_1 = open('customers.txt','r',encoding='utf-8')
fh_2 = open(filename,"a",encoding="utf-8")

print(f"{file_copy_n(fh_1,fh_2,5)}")

fh_1.close()
fh_2.close()

