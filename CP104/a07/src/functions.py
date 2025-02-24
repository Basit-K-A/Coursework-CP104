"""
------------------------------------------------------------------------
Assignment 7, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-17"
------------------------------------------------------------------------
"""

def list_factors(number):
    """
    -------------------------------------------------------
    takes an integer > 0 and return a lost of the factors that
    make up that number excepting the number itself
    Use: list_factors - a number > 0
    -------------------------------------------------------
    Parameters:
        number - integer > 0
    Returns:
        factors - list of factors
    ------------------------------------------------------
    """
    factors = []
    n = 1
    while n != number:
        if number%n == 0: factors.append(n)
        n += 1
    return factors

def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    inp = int
    number_list = []
    while inp != 0:
        inp = int(input("Enter a positive number: "))
        if inp > 0: number_list.append(inp)
    return number_list

def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []
    for i in range(len(numbers)):
        if numbers[i] == target_number: index_list.append(i)
    return index_list

def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    rem = []
    for j in range(len(subtrahend)):
        for i in range(len(minuend)):
            if minuend[i] == subtrahend[j]: rem.append(minuend[i])
    for i in range(len(rem)):
        minuend.remove(rem[i])

    return

def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    index = -1
    in_order = True
    
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            in_order = False
            index = i+1
            break
        
    if in_order == True: index = -1

    return in_order, index