"""
------------------------------------------------------------------------
Assignment 9, functions
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    
    line = file_handle.readline()
    i = 1
    
    while i != count+1 and line != "":
        print(f"{line}",end="")
        line = file_handle.readline()
        i += 1
        
    return

def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    
    line = file_handle.readline()
    number_list = []
    
    while line != "":
        
        data = line.strip().split(",")
        line = file_handle.readline()
        
        for i in range(len(data)):
            if data[i].isdigit():number_list.append(int(data[i]))
            
    return number_list

def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    line = file_handle.read()
    n = len(line)
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = n
    
    for i in range(n):
        if line[i].isupper():ucount+=1;rcount-=1
        if line[i].islower():lcount+=1;rcount-=1
        if line[i].isdigit():dcount+=1;rcount-=1
        if line[i].isspace():wcount+=1;rcount-=1
    return ucount,lcount,dcount,wcount,rcount

def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    this is partially okay
    """
    line = fh_read.readline()
    count = 0
    fh_write.write(f"{'['}{count}{'] '}{line}")
    fh_write.write(f"{'['}{count+1}{']'}{' '}")
    count+=2
    
    for line in fh_read:
        line = fh_read.readline()
        fh_write.write(f"\n{'['}{count}{'] '}{line}")
        fh_write.write(f"{'['}{count+1}{']'}{' '}")
        count +=2
    return

def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    line = file_handle.readline()
    temp = []
    h = 0
    total = 0
    count = 0
    
    while line != "":
        
        data = line.strip().split(',')
        
        if (len(temp)) != 0:
            if data[3] > temp[3]: l_id = temp[2]
            
            if int(data[3]) > h:
                h_id = data[2]
                h=int(data[3])
                
                
        temp = data
        line = file_handle.readline()
        total += int(data[3])
        count += 1
    avg = total/count
    
    return l_id, h_id,avg
    