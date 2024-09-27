"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0.00
# Number of characters.
numChars = 20
# Color of characters.
color = "gold"
# Type of wood.
woodType = "pine"

# Write assignment and if statements here as appropriate.
if numChars > 5:
    charge = 35 + (numChars-5)*4
elif numChars > 0:
    charge = 35

if woodType == "oak":
    charge += 20

if color == "gold":
    charge += 15      

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
