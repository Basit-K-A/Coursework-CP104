"""
------------------------------------------------------------------------
Lab 3, task 8
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-25"
------------------------------------------------------------------------
"""

dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel(m^3): "))
sand = float(input("Enter amount of sand(m^3): "))

total = dirt+gravel+sand

print(f"""
Material    Cubic Metres
Dirt  {dirt:>6.1f}
Gravel{gravel:>6.1f}
Sand  {sand:>6.1f}
Total {total:>6.1f}
""")