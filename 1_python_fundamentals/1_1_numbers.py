# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.1: Data Identification - Numbers and Math Operators
blank = "----------------------"

# Data Identificaiton Rules
# 1. Variable cannot start with number 
# 2. Upper case and lower case sensitive
# 3. Do not use Turkish characters
# 4. Use "_"

# IMPORTANT
# Instead of identify variables one by one use this method:
x, y, name, isTrue = (4, 3.3, "Alice", True)

# Integer: a number which is not a fraction; a whole number
number_int = 3
print(type(number_int))

# Floating Number Point: is a positive or negative whole number with a decimal point
number_float = 3.4
print(type(number_float))
print(blank)

##############################################################################################################

# Addition
num1 = 44
num2 = 22
add = num1 + num2
print("Addition = ", add) # 66

# Subtraction
sub = num1 - num2
print("Subtraction = ", sub) # 22

# Multiplication
multiply = num1 * num2
print("Multiplication = ", multiply) # 968

# Division
divide = num1 / num2
print("Division = ", divide) # 2.0 result is given as floating point number

# Exponentiation
exp = num1 ** num2
print("Exponentiation = ", exp) # 1432052311740255546466984939315265536

# Modulus
mod = num1 % num2
print("Modulus = ", mod) # 0

# Full Division
fd = num1 // num2
print("Full Division = ", fd) # 2 result is given as integer number
print(blank)

##############################################################################################################

# Example 1: Salary Calculation
salary_of_Alice = 7000
salary_of_Bob = 6000
tax = 0.27
print("Net Salary of Alice = ", salary_of_Alice - (salary_of_Alice * tax)) # 5110.0
print("Net Salary of Bob = ", salary_of_Bob - (salary_of_Bob * tax)) # 4380.0
print(blank)

##############################################################################################################

# Example 2: Form the given variables for a customer
"""
Customer's name
Customer's surname
Customer's name + surname
Customer's gender
Customer's ID No
Customer's birth year
Customer's adress
Customer's age

"""
c_name = 'Alice'
c_surname = 'Cipher'
c_n_s = c_name + ' ' + c_surname
c_gender = 'Female' # may referred as True or False
c_ID = '123456789'
c_birth_year = 1995
c_adress = 'Caribbean Islands'
c_age = 2022 - c_birth_year
print(blank)

##############################################################################################################

# Example 3: Calculate the total information of the orders placed
"""
Order 1 = 110 TL
Order 2 = 1100.5 TL
Order 3 = 356.95 TL

"""
order_1 = 110
order_2 = 1100.5
order_3 = 356.95
overall = order_1 + order_2 + order_3
print('Total information of the orders placed = ', overall, 'TL') # 1567.45 TL


