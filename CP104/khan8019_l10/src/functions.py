"""
------------------------------------------------------------------------
Lab 10, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
#3, 5, 8, 12, 14

def customer_best(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    line = fh.readline()
    temp = []
    
    while line != "":
        data = line.strip().split(',')
        if (len(temp)) != 0:
            if data[3] > temp[3]: result = temp
        temp = data 
        line = fh.readline()
        
    return result

def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    line = fh.readline()
    while line != "":
        line = fh.readline()
        
    fh.write(f"\n")
    
    for i in range(len(fields)):
        if i == len(fields)-1:
            fh.write(f"{fields[i]}")
        else: fh.write(f"{fields[i]},")
    #fh.close()
    return

def append_increment(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of the fh. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    line = fh.readline()
    while line != "":
        dig = int(line)
        print(dig)
        line = fh.readline()
        
    dig+=1
    fh.write(f"{dig}")
    return dig

def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    line = fh.readline()
    word = line.strip()

    while line != "":
        line = line.strip()
        if len(line) < len(word):
            word = line
        line = fh.readline()

    return word

def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    line = fh_1.readline()
    
    for i in range(n):
        fh_2.write(f"{line}")
        line = fh_1.readline()
        i+=1
    
    return
        