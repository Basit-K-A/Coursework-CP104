"""
------------------------------------------------------------------------
Lab 5, Functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-15"
------------------------------------------------------------------------
"""
from unicodedata import category
def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    GRAVITY = 9.8
    
    weight = mass*GRAVITY
    
    if(weight > 1000):
        message = "heavy"
    elif(weight < 10):
        message = "light"
    else:
        message = "average"
        
    return weight,message


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if(year%4==0 and year%100!=0):
        result = True
    elif(year%400==0):
        result = True
    else:
        result = False
        
    return result

def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    BREEZE = 39
    STRONGWIND = 61
    GALEWINDS = 88
    WHOLEGALE = 117


    if speed<0:
        category = "Unknown"
    
    elif speed<BREEZE :
        category = "Breeze"
        
    elif speed<=STRONGWIND:
        category = "Strong Wind"
        
    elif speed<=GALEWINDS:
        category = "Gale Winds"
        
    elif speed<=WHOLEGALE:
        category = "Whole Gale"
        
    else:
        category = "Hurricane"
    
    return category


def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    if x == 0 and y == 0:
        location = "Origin"
    elif x > 0 and y > 0:
        location = "Quadrant 1"
    elif x < 0 and y < 0:
        location = "Quadrant 3"
    elif x > 0 and y < 0:
        location = "Quadrant 4"
    elif x < 0 and y > 0:
        location = "Quadrant 2"
    elif x == 0 and y != 0:
        location = "Y-Axis"
    else:
        location = "X-Axis"
    
    return location

def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    INFANT = 3
    KID = 10
    STUDENT = 18
    ADULT = 65
    
    age = int(input("How old are you? "))
    
    if age <= INFANT:
        price = 0
        
    elif age < KID:
        price = 2
        
    elif age < STUDENT:
        studer = input("Are you a student of this school? ")
        
        if(studer == "Y"):
            price = 1
        else:
            price = 3
            
    elif age < ADULT:
        price = 5
    else:
        price = 4
        
    return price
    
        
        