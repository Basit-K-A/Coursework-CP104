"""
------------------------------------------------------------------------
functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-21"
------------------------------------------------------------------------
"""

def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    -------------
    """
    sume = 0
    for i in range(start,finish+1,increment):
        sume += i
    return sume

def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    
    if height!=0:print(" " * (height-1) + char) #prints first row
    
    for i in range(1, height - 1): #prints intermediate rows
        spaces = " " * (height - i - 1)
        print(spaces + char * (2 * i + 1))
        
    if height > 1:print(char * (2 * height - 1))#prints last row
    
    return None

def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(1,width):
        print(char*(i))
    for i in range(width,0,-1):
        print(char*(i))
        
    return None

def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    print(f"{'Year':<s}{'Value    $':>9s}\n--------------")
    print(f"{0:2.0f}{value: >12,.2f}")
    
    for i in range(1,years+1):
        value += ((rate/100))*value
        print(f"{i:2.0f}{value: >12,.2f}")
        
    final_value=value
    return final_value

def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    print("""              Cross-Sectional  Moment of  Section
Base  Height  Area             Inertia    Modulus
-------------------------------------------------""")
    
    for i in range(b_min,b_max+1,b_inc):
        for j in range(h_min,h_max+1,h_inc):
            cArea = i*j
            mInert = (i*j**3)/12
            secMod = (i*j**2)/6
            print(f"{i:2.0f}{'x':>4s}{j:>4d}{cArea:>10.2f}{mInert:>15.2f}{secMod:>14.2f}")
    return None
    