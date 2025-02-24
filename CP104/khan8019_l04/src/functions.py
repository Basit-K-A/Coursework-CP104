"""
------------------------------------------------------------------------
Lab 4, Functions for tasks
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from math import pi, sqrt
def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: circ = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        circ - circumference of a circle (float)
    ------------------------------------------------------
    """ 
    circ = float(2*pi*radius)
    
    return circ

def right_triangle(adjacent, opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, perimeter, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, per, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        per - perimeter of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """
    hyp = sqrt((adjacent)**2+(opposite)**2)
    per = hyp + opposite + adjacent
    area = (adjacent*opposite)/2
    
    return hyp,per,area

def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    pre_commision_cost = float(computer_cost*computers_bought)
    
    commision_amount = (commission_percent/100)*pre_commision_cost
    
    total_cost = float(pre_commision_cost+commision_amount)
    
    return pre_commision_cost,total_cost
    
def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    FAHRENHEIT_FREEZING = 32    
    
    fahrenheit = ((9/5)*celsius + FAHRENHEIT_FREEZING)
    
    return fahrenheit


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    DAY_FROM = 86400
    HOURS_FROM = 3600
    MINS_FROM = 60
    
    days = initial_seconds//DAY_FROM
    dayRem = initial_seconds%DAY_FROM
    
    hours = dayRem//HOURS_FROM
    hoursRem = dayRem%HOURS_FROM
    
    minutes = hoursRem//MINS_FROM
    minRem = hoursRem%MINS_FROM
    
    seconds = minRem
    
    return days,hours,minutes,seconds
        