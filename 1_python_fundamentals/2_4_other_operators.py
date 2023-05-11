# BTK Academy
# Advanced Python Programming From Zero
# Lecture 2.3: Python Operators - Other Operators
# python 2_4_other_operators.py
blank = "----------------------"

# Identity Operator : is
# This operator compares 'reference adresses' of lists. If the elements are the same for different two list
# adresses won't be the same.

x = y = [1, 2, 3] # address is the same
z = [1, 2, 3] # addres between x and z is different

print(x == y) # True
print(x == z) # True
print(blank)

print(x is y) # True
print(x is z) # False
print(x is not z) # True
print(blank)

##############################################################################################################

# Membership Operator : in
# Checks for the desired element in a list
a = ['hatter', 'absolem', 'chess']
print('chess' in a) # True
print('chess' not in a) # False
