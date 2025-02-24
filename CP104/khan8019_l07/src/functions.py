"""
------------------------------------------------------------------------
Lab 7, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-30"
------------------------------------------------------------------------
"""
from random import randint 


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    guess = int
    count = 0
    
    
    while(guess!=number):
        guess = int(input("Guess: "))
        if guess>number:print("Too high")
        else:print("Too low")
        count +=1
        
    print("Congratulations - Good Guess")
    print(f"you made {count} guesses.") 
    
    return count 

def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1
    
    count = 0
    
    while power < target:
        power = 2**count
        count += 1
        
    return power

def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    
    
    posValue = (float(input("First Positive Value: ")))
    inpNum = []
    inpNum.append(posValue)
    
    while posValue>0:
        posValue = (float(input("Next Positive Value: ")))
        if posValue>0:inpNum.append(posValue)
        
    minimum = min(inpNum)
    maximum = max(inpNum)
    total = sum(inpNum)
    average = total/(len(inpNum))
    
    return minimum, maximum, total, average

def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    expenses = 0
    
    inpExp = float(input("Enter an expense(0 to quit): "))
        
    while inpExp!=0:
        expenses += inpExp
        inpExp = float(input("Enter another expense (0 to quit): "))
        
    balance = available-expenses
    
    if balance > available:
        status = "Surplus"
    elif balance < available:
        status = "Deficit"
    else:
        status = "Balanced"
    
    return expenses, balance, status

def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    empID = int
    allP = []
    
    TAX = 3.625
    STHOURS = 40
    OVT = 1.5
    
    while empID!=0:
        
        empID = int(input("Employee ID (0 to quit): "))
        if empID==0: break
        
        wageRate = float(input("Hourly wage rate: "))
        hWorked = float(input("Hours worked: "))
        
        if hWorked<=STHOURS:
            taxAm = (hWorked*wageRate)*(TAX/100)
            netPay = (hWorked*wageRate)-taxAm
            print(f"Net payment for employee {empID}: {netPay:.2f}")
            
        else:
            taxAm = ((STHOURS*wageRate)+((hWorked-STHOURS)*(wageRate*OVT)))*(TAX/100)
            netPay = ((STHOURS*wageRate)+((hWorked-STHOURS)*(wageRate*OVT)))-taxAm
            print(f"Net payment for employee {empID}: {netPay:.2f}")
            
        allP.append(netPay)
    
    total = sum(allP)
    average = total/(len(allP))
    
    return total, average
        
        
        