"""
------------------------------------------------------------------------
Assignment 8, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-11-25"
------------------------------------------------------------------------
"""

def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    n = len(sentence)
    temp = 0
    spaced = ""
    
    for i in range(n):
        if i != 0:
            if sentence[i].isupper():
                new = sentence[temp:i]
                if temp == 0:spaced += new
                else:spaced += " " + new.lower() 
                temp = i
    new = sentence[temp:n]
    spaced += " " + new.lower()
    
    return spaced

def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    pluralized = string
    
    if string.endswith("s") or string.endswith("sh") or string.endswith("ch"):
        pluralized += "es"
    elif string.endswith("y") and not string.endswith("ay") and not string.endswith("oy"):
        pluralized = string[0:len(string)-1]
        pluralized += "ies"
    else:
        pluralized += "s"
        
    return pluralized

def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    suffix = ""
    same = True
    count = -1
    
    while same == True and -count != len(str1)+1 and -count != len(str2)+1:
        if str1[count] == str2[count]:
            suffix += str2[count]
            count -= 1
        else: same = False
        
    suffix = suffix[::-1]  
    return suffix

def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    group = 1
    
    is_valid = True
    for i in range(len(isbn)):
        if len(isbn) != 17:
            is_valid = False
        if isbn[i].isdigit() == False and "-" not in isbn[i]:
            is_valid = False
        if isbn[-2] != "-":
            is_valid = False
        if isbn[0:3] != "978" and isbn[0:3] != "979":
            is_valid = False
        if isbn[i].isdigit():
            lastwasdig = True
        if "-" in isbn[i] and lastwasdig:
            group += 1
            lastwasdig = False
            
    if group != 5: is_valid = False
    
    return is_valid

def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    n = len(words)
    temp = ""
    count = 1
    i = 0
    word_chain = True
    
    while word_chain == True and count != n-1:
        if i != 0:
            if words[i][0] == temp[0]:
                count += 1
            else: word_chain = False
        i+=1
        temp = words[i]
        
    
    return word_chain
            