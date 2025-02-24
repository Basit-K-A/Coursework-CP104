"""
------------------------------------------------------------------------
Lab 11, task 1
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import generate_matrix_num,print_matrix_num
matrix = generate_matrix_num(3, 4, -10, 10, 'int')

print(f"{print_matrix_num(matrix,'float')}")