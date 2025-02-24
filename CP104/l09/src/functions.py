"""
------------------------------------------------------------------------
Lab 9, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-11-17"
------------------------------------------------------------------------
"""
#1, 3, 7, 10, 14

def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    hydroxide = False
    
    if chemical.endswith("OH"):
        hydroxide = True
    
    return hydroxide

def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:11]
    return pc, pi, pq

def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    n = len(s)
    count = 0
    s = s.lower()
    
    for i in range(n):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            count += 1
    return countf

def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    n = len(txt)
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    
    for i in range(n):
        if txt[i].isupper():
            uppr += 1
        elif txt[i].islower():
            lowr += 1
        elif txt[i].isdigit():
            dgts += 1
        elif txt[i].isspace():
            whtspc += 1
            
    return uppr, lowr, dgts, whtspc

def str_distance(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    count = 0
    
    n = len(s1)
    
    if len(s1) == len(s2):
        for i in range(n-1):
            if s1[i] != s2[i]:
                count += 1
            else:
                break
    else: count = -1
    
    if count > 0: count+=1
    
    return count