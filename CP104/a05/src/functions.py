"""
------------------------------------------------------------------------
Assignment 5, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-11-04"
------------------------------------------------------------------------
"""

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    
    for i in range(1,number+1,1):
        product *= i
    return product

def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    prints a table of the number of calories burned every five minutes
    given the number of calories burned per minute (per_min) an the total number of minutes run (minutes).
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per min
        minutes - number of minutes runnning for
    Returns:
        none
    ------------------------------------------------------
    """
    
    for i in range(5,minutes+1,5):
        calBurned = per_min*i
        print(f"{i:>2}{calBurned:^15.1f}")
    return

def arrow_up(rows):
    """
    -------------------------------------------------------
    prints a hollow upward pointing triangle given a specified
    amount of rows
    Use: rows = arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows for the triangle
    Returns:
        none
    ------------------------------------------------------
    """
    spaces = ' '*(rows-1)
    if rows >0:
        print(f"{spaces}{'#'}")
        
        for i in range(1,rows-1,1):
    
            print(f"{' '*((rows-i)-1)}{'#'}{' '*((i*2)-1)}{'#'}")
        
        if rows != 1:print(f"{'#'}{' '*((rows*2)-3)}{'#'}")
    return

def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("",end="")
    for k in range(start_num,stop_num+1,1):
        print(f"{k:3d}",end="")
    print("")
    print('--------------------')
    
    for j in range(start_num,stop_num+1,1):
     
        print(f"{j:2d}{'|'}",end="")
        
        for i in range(start_num, stop_num + 1):
            product = i * j
            print(f"{product:3d}", end="")
        print()
        
    return

def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    end = count*increment
    sume = 0
    
    for i in range(start,end+1,increment):
        sume += i
    return sume