"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from functions import line_numbering

fh_1 = open("wilde.txt","r",encoding="utf-8")
fh_2 = open("wilde_numbered.txt","w",encoding="utf-8")

print(f"{line_numbering(fh_1,fh_2)}")

fh_1.close()
fh_2.close()