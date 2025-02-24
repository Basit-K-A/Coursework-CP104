"""
------------------------------------------------------------------------
Lab 11, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
#1, 3, 6, 8, 13
from random import randint,uniform

def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    
    for i in range(rows):
        row = []
        for j in range(cols):
            if value_type=="int": row.append(randint(low,high))
            else: row.append(uniform(low,high))
        matrix.append(row)
        
    return matrix

def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    for i in range(len(matrix[0])):
        print(f"{i:>7d}",end="")
    print("")
    for i in range(len(matrix)):
        print(f"{i}",end="")
        for j in range(len(matrix[0])):
            if value_type=="int":print(f"{matrix[i][j]:>5d}",end="")
            else:print(f"{matrix[i][j]:>8.2f}",end="")
        if i != len(matrix)-1:print("")
        
    return

def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """ 
    total = 0
    smallest = matrix[0][0]
    largest = matrix[0][0]
    
    for i in range(len(matrix)):
        
        for j in range(len(matrix[0])):
            total += matrix[i][j]
            if matrix[i][j] > largest: largest = matrix[i][j]
            if matrix[i][j] < smallest: smallest = matrix[i][j]
    average = total/(len(matrix)*len(matrix[0]))
                     
    return smallest,largest,total,average

def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    loc = []
    #less = True

    for i in range(len(matrix)):
        if matrix [i][i] < n:
            loc.append(i)
            loc.append(i)
            break
        for j in range(len(matrix[0])):
            if matrix[i][j] < n: 
                loc.append(i)
                loc.append(j)
                break
    return loc

def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j]*num
    return