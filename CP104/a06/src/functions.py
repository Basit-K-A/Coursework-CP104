"""
------------------------------------------------------------------------
Assignment 6, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-11-08"
------------------------------------------------------------------------
"""

def total_wins():
    """
    -------------------------------------------------------
    Determines the amount of wins for a team
    Use: wins(purple,gold) = total_wins()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        winPurple, winGold    
    ------------------------------------------------------
    """
    winPurple = 0
    winGold = 0
    
    team = input("Enter the winning team: ")
    
    while team!="":
        if team == "purple": winPurple+=1
        if team == "gold": winGold+=1
        team = input("Enter the winning team: ")
    return winPurple, winGold

def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    i = 1
    factors = 0
    
    while i != number+1:
        if number%i == 0: factors += 1
        i +=1
        
    if factors == 2: prime = True
    else: prime = False
    
    return prime

def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"""
    Principal: ${principal_amount:.2f}
    Interest rate: {interest_rate:.2f}%
    Monthly payment: ${payment:.2f}
    ----------------------------------
    Month Interest   Payment   Balance
    ----------------------------------""")
    month = 1
    balance = principal_amount
    
    while balance >= payment:
        interest = (balance*((interest_rate/100)/12))
        balance = balance-(payment) + interest
        
        print(f"{month:>6}{interest:10.2f}{payment:^12.2f}{balance:>12.2f}")
        
        month +=1
        
    last = (balance*((interest_rate/100)/12))
    balance += last
    finPay = balance
    balance -= balance
    
    print(f"{month:>6}{last:10.2f}{finPay:^12.2f}{balance:>12.2f}")
    return
     
def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    nint = int
    count = 0
    
    while nint != 0:
        if number > 0:nint = number//10
        else: nint = number//-10
        number = nint
        count+=1
    return count
    
def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    i = 1
    factors = []
    
    while i != number:
        if number%i == 0: factors.append(i)
        i += 1
        
    total = sum(factors)
    return total
    