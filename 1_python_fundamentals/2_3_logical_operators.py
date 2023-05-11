# BTK Academy
# Advanced Python Programming From Zero
# Lecture 2.3: Python Operators - Logical Operators
# python 2_3_logical_operators.py
blank = "----------------------"

# Logical Operators
x = 7
logic_1 = 3 < x < 14
print(logic_1)
print(blank)

##############################################################################################################

# AND Operator
right = 3
cntn = 'c'
l_and = (x > 7) and (x < 14)  # in this situation if both comparisons are true result will be true
l_and_2 = (cntn == 'c') and (right < 3)
print(l_and)
print(l_and_2)
print(blank)

# OR Operator
l_or = (x > 4) or (x % 5 == 0) # in this situation if both comparisons are not false result will always be true
print(l_or)
print(blank)

# NOT Operator
l_not = not(x > 8)
print(l_not)
print(blank)

##############################################################################################################

# Practice 1: Is y is a number that even and between 5 - 10?
y = int(input("Please enter the y: "))
y_r = (y % 2 == 0) and (5 < y < 10)
print(f"y situation is {y_r}")

##############################################################################################################

# Example 1 : Working with logical operators

# 1 - Check the entered number if it's between 0 - 100.
num = int(input("Please enter the number: "))
interval = 0 < num < 100
print(f"Entered number is {num} and interval situation is {interval}")
print(blank)

##############################################################################################################

# 2 - Print whether the entered number is positive and even.
pos_even = (num > 0) and (num % 2 == 0)
print(f"Entered number is {num} and positive and even situation is {pos_even}")
print(blank)

##############################################################################################################

# 3 - Check login with email and password.
u_email = "alice@wonderland.com"
u_passwd = "them@dh@tter!"
email = input("Please enter your e-mail adress: ")
passwd = input("Please enter your password: ")
login = (email == u_email) and (passwd == u_passwd)
print(f"According to entered information login success is {login}")
print(blank)

##############################################################################################################

# 4 - Compare three entered number according to their values.
n_1 = int(input("Please enter the first number: "))
n_2 = int(input("Please enter the second number: "))
n_3 = int(input("Please enter the third number: "))
print(f"1st number is greater than 2nd number {n_1 > n_2}.\n1st number is greater than 3rd number {n_1 > n_3}.\n2nd number is greater than 3rd number {n_2 > n_3} ")
print(blank)

##############################################################################################################

# 5 - Get two midterm and one final exam results from the user. Percentanes will be %60 for midterm and %40 for final exam.
# If grade average is greater and equal to the 50 print 'Passed' else print 'Failed'.
# Even grade average is 50 final exam grade must be at least 50.
# If final exam grade is 70 grade average is not important.

mid_1 = int(input("Please enter the first midterm exam result: "))
mid_2 = int(input("Please enter the second midterm exam result: "))
final = int(input("Please enter the final exam result: "))
average = (((mid_1 + mid_2)//2)*0.6) + (final*0.4)

pass_situation = (average >= 50 and final >= 50) or final >= 70
print(f"Grade avergae is {average} student pass situation is {pass_situation}.")
print(blank)

##############################################################################################################

# 6 - Get name, weight and height information from user and calculate BMI .
# Formula = weight / height ** 2
# 0 - 18.4 = Weak 
# 18.5 - 24.9 = Normal
# 25.0 - 29.9 = Overweight
# 30.0 - 34.9 = Obese

name = input("Please enter your name: ")
weight = int(input("Please enter your weight: "))
height = int(input("Please enter your height: "))
bmi = ((weight) / (height ** 2)) * 100
weak = 0 <= bmi <= 18.4
normal = 18.5 <= bmi <= 24.9
overweight = 25.0 <= bmi <= 29.9
obese = 30.0 <= bmi <= 34.9
print(f"BMI Situtaion: {bmi}\nWeak: {weak}\nNormal: {normal}\nOverweight: {overweight}\nObese: {obese}")


