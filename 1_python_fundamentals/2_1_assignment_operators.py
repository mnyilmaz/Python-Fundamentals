# BTK Academy
# Advanced Python Programming From Zero
# Lecture 2.1: Python Operators - Assignment Operators
# python 2_1_assignment_operators.py
blank = "----------------------"

# Assignment Operators
x, y, z = 5, 10, 20
print(x,y,z)
print(blank)

##############################################################################################################

# Mathmetical Operators
x += 5
print("After additon operator x is: ", x)
print(blank)

x -= 7
print("After subtraction operator x is: ", x)
print(blank)

x *= 4 
print("After multiplication operator x is: ", x)
print(blank)

x /= 6
print("After divison operator x is: ", x)
print(blank)

x **= 8
print("After exponantion operator x is: ", x)
print(blank)

x %= 2
print("After modulus operator x is: ", x)
print(blank)

x //= 3
print("After full divison operator x is: ", x)
print(blank)

values = 1, 2, 3, 4, 5
print(type(values))

a, b, *c = values # normally values are including more elements that a, b, c can get
print(a, b, c) # *c is assigning remaining elements into c as a list

##############################################################################################################

# Example 1 : Working with assignment operators
q, w, e = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1 - What is the difference between the product of the two numbers you get from the user and the sum of q, w, e?
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))
sum = q + w + e
result = ((num_1 * num_2) - sum )
print("Sum =", sum)
print("Result =", result)
print(blank)

##############################################################################################################

# 2 - Divide w by e without remainder.
w //= q
print("w/e =", w)
print(blank)

##############################################################################################################

# 3 - What is the mod 3 of the sum of q, w and e?
sum %= 3
print("Mod 3 of sum =",sum)
print(blank)

##############################################################################################################

# 4 - Calculate q power of w. 
w **= q
print("q power of w =", w)
print(blank)

##############################################################################################################

# 5 - Use q, *w, e = numbers and according to the result calculate the cube of e.
q, *w, e = numbers
print(q, w, e)
e **= 3
print("Cube of e is =", e)
print(blank)

##############################################################################################################

# 6 - According to process from previous question, what is the sum of values that w include?
sum_w = w[0] + w[1] + w[2]
print("Sum of w list is =", sum_w)
 