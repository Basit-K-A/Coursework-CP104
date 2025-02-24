"""
------------------------------------------------------------------------
Assignment 4, Functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-21"
------------------------------------------------------------------------
"""

def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7
    
    if day_num==SUNDAY:day = "Sunday"
    elif day_num==MONDAY:day = "Monday"
    elif day_num==TUESDAY:day = "Tuesday"
    elif day_num==WEDNESDAY:day = "Wednesday"
    elif day_num==THURSDAY:day = "Thursday"
    elif day_num==FRIDAY:day = "Friday"
    elif day_num>FRIDAY<8:day="Saturday"
    else:day = "Error"
    return day

def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy" for Sensitive Groups - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    GOOD = 50
    MODERATE = 100
    UNHEALTHYSENS = 150
    UNHEALTHY = 200
    VERYUNHEALTHY = 300
    
    if air_quality_index<=GOOD:pollution="Good"
    elif air_quality_index<=MODERATE:pollution="Moderate"
    elif air_quality_index<=UNHEALTHYSENS:pollution="Unhealthy for Sensitive Groups"
    elif air_quality_index<=UNHEALTHY:pollution="Unhealthy"
    elif air_quality_index<=VERYUNHEALTHY:pollution="Very Unhealthy"
    elif air_quality_index>VERYUNHEALTHY:pollution="Hazardous"
    else:pollution="Error"
    return pollution
    
def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    if val1>val2>val3 or val2>val1>val3:
        average = (val1+val2)/2
    elif val2>val3>val1 or val3>val2>val1:
        average = (val2+val3)/2
    else:
        average = (val3+val1)/2
    return average

def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if rgb_colour1 == "red" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "red":
        rgb_colour = "fuchsia"
    elif rgb_colour1 == "red" and rgb_colour2 == "green" or rgb_colour1 == "green" and rgb_colour2 == "red":
        rgb_colour =  "yellow"
    elif rgb_colour1 == "green" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "green":
        rgb_colour =  "aqua"
    elif rgb_colour1 == "red" and rgb_colour2 == "red":
        rgb_colour =  "red"
    elif rgb_colour1 == "blue" and rgb_colour2 == "blue":
        rgb_colour =  "blue"
    elif rgb_colour1 == "green" and rgb_colour2 == "green":
        rgb_colour =  "green"
    else:
        rgb_colour =  "Error"
    return rgb_colour

def hoo_rah(number):
    """
    -------------------------------------------------------
    hoo_rah takes an integer parameter and returns one of the following strings:

    "Hoo" if number is evenly divisible by 2
    "Rah" if number is evenly divisible by 7
    "Hoo Rah" if number is evenly divisible by both 2 and 7
    "Zip" if number is none of the above
    
    Use: hooStr = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number - any integer
    Returns:
        hooStr - a string depending on the initial int    
    """
    
    if number%2==0:hooStr="Hoo"
    elif number%7==0:hooStr="Rah"
    elif number%2==0 and number%7==0:hooStr="Hoo Rah"
    else:hooStr="Zip"
    return hooStr
