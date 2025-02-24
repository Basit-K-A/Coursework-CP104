"""
------------------------------------------------------------------------
Assignment 2, task 5
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-10-04"
------------------------------------------------------------------------
"""

fLength = float(input("Foundation length (m): "))
fWidth = float(input("Foundation width (m): "))
fHeight = float(input("Foundation height (m): "))
wHeight = float(input("Wall height (m): "))
concCost = float(input("Cost of concrete ($/m^3): "))
brickCost = float(input("Cost of bricks ($/m^2): "))

concNeed = (fLength*fWidth*fHeight)
concTotal = concCost*concNeed

brickNeed = 2*(wHeight*fLength + wHeight*fWidth)
brickTotal = brickCost*brickNeed

total = brickTotal+concTotal

print(f"""
Concrete needed for foundation (m^3): {concNeed:,.2f}
Cost of concrete: ${concTotal:,.2f}
Bricks needed for walls (m^2): {brickNeed:,.2f}
Cost of bricks: ${brickTotal:,.2f}
Total cost: ${total:,.2f}
""")