# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.2: Data Identification - Type Conversion
blank = "----------------------"

import math

x = input('Number 1: ') # in here data will be 'string' so you have to convert string to int
y = input('Number 2: ')
sum = int(x) + int(y)
print(sum) # result will be given as string unless you don't conver result to string
print(blank)

# Ctrl + k + c to comment them all or use ''' or """

a = 5            # int --> print(type(a))
b = 4.5          # float --> print(type(b))
name = "Alice"   # string --> print(type(name))
isOnline = True  # bool --> print(type(isOnline))

# Convert int to float
x = float(x)
print(type(x))

# Convert float to int
b = int(b)
print(type(b))

# Convert int to string
a = str(a)
print(type(a))

# Convert bool to string
isOnline = str(isOnline)
print(type(isOnline))
print(blank)

# Convert bool to int
# isOnline = int(isOnline) # is bool is true int value will occur as '1' if false it will be '0'
# print(type(isOnline))

##############################################################################################################

# Example 1: Calculate the area and perimeter of a circle for a given radius

"""
Cirle Area Formula :  πr2
Circle Perimeter Formula :  2πr
Given Radius = 3.14
"""

r = input("Perimeter: ")
r = int(r)
c_area = (r ** 2) * math.pi
print("Area of the circle is: ", c_area)
c_perimeter = 2 * math.pi * r 
print("Perimeter of the circle is: ", c_perimeter)


