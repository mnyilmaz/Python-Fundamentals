# BTK Academy
# Advanced Python Programming From Zero
# Lecture 2.2: Python Operators - Comparison Operators
# python 2_2_comparison_operators.py
blank = "----------------------"

# Comparison Operators
a, b, c, d = 5, 30, 20, 30

result_1 = a == b # False
result_2 = a == c # False
result_3 = a == d # False
result_4 = b == c # False
result_5 = b == d # True
result_6 = c == d # False
print("Result 1 is =",result_1)
print("Result 5 is =",result_5)
print(blank)

user_name = 'alice'
password = 'wonderland'
login_u = ('alc' == user_name)
login_p = ('wonderland' == password)
print(f"User name is {login_u} and password is {login_p}.")
print(blank)

##############################################################################################################

# is Equal
a == b

# is not Equal
a != b # prints TRUE if a does not equal to b

# is Greater
a > b

# is Less than
a < b

# is Greater and Equal
a >= b

# is Less than and Equal
a <= b

# True is equal to 1 as numerical  -->  True == 1
# False is equal to 0 as numerical -->  False == 0

##############################################################################################################

# Example 1 : Working with comparison operators

# 1 - Which of the two numbers entered is greater?
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))
result = num_1 > num_2
print(f"First number is {num_1} and second number is {num_2}. {num_1} > {num_2} is {result}")
print(blank)

##############################################################################################################

# 2 - Get two midterm and one final exam results from the user. Percentanes will be %60 for midterm and %40 for final exam.
# If grade average is greater and equal to the 50 print 'Passed' else print 'Failed'.

mid_1 = int(input("Please enter the first midterm exam result: "))
mid_2 = int(input("Please enter the second midterm exam result: "))
final = int(input("Please enter the final exam result: "))
average = (((mid_1 + mid_2)//2)*0.6) + (final*0.4)

if average >= 50:
    print(f"Grade avergae is {average} student has passed this lesson.")
else:
    print(f"Grade avergae is {average} student has failed this lesson.")

# print(f"Grade avergae is {average} student situation is {average >= 50}.")
print(blank)

##############################################################################################################

# 3 - Print whether the entered number is odd or even.
n = int(input("Please enter the number: "))

if n % 2 == 0:
    print(f"Entered number is {n} and it is an even number.")
else:
    print(f"Entered number is {n} and it is an odd number.")

# print(f"Entered number is {n} and number situation is {n % 2}.")
print(blank)

##############################################################################################################

# 4 - Print whether the entered number is positive or negative.
n = int(input("Please enter the number: "))

if n > 0:
    print(f"Entered number is {n} and it is a positive number.")
else:
    print(f"Entered number is {n} and it is a negative number.")

# print(f"Entered number is {n} and number situation is {n > 0}.")
print(blank)

##############################################################################################################

# 5 - Get email and password information from the user and check the accuracy.
u_mail = "alice@wonderland.com"
u_passwd = "them@dh@tter!"

email = input("Please enter your e-mail adress: ")
passwd = input("Please enter your password: ")

if email == u_mail:
    if passwd == u_passwd:
        print(f"Login successfully")
if email != u_mail:
    print(f"Entered mail is {email} and it is not correct. Try again")
if email == u_mail:
    if passwd != u_passwd:
        print("Wrong Password!")

# print(f"Login situaiton is {email == u_mail and passwd == u_passwd}.")
print(blank)




