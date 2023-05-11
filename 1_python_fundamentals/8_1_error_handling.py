# BTK Academy
# Advanced Python Programming From Zero
# Lecture 8.1: Erros and Error Handling in Python
# python 8_1_error_handling.py
from distutils import file_util
from unicodedata import name


blank = "----------------------"

# Error Handling
# When these exceptions occur, the Python interpreter stops the current process and passes it 
# to the calling process until it is handled. If not handled, the program will crash.

# print(a) -> Name Error
# int("234") -> Value Error
# print(10/0) -> Zero Division Error
# print("tr"y) - > Syntax Error

# while True:
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except ZeroDivisionError:
    print("y cannot be 0")
except ValueError:
    print("x or y cannot include char")
else:
    print("Everything seems right.")
    # break
finally:
    print("Try-Except has ended") # finally blok works all the time

# or except (ZeroDivisonError, ValueError) as e:
#       print("Invalid input")
#       print(e) -> that allows private warning per error   
print(blank)

##############################################################################################################

# Raising an Exception

# z = 10
# if z > 7:
#     raise Exception("z cannot be bigger than 7")

def check_passwd(passwd):
    import re
    if(len(passwd)) < 8:
        raise Exception("Password must be at least 7 characters")
    elif not re.search("[a-z]", passwd):
        raise Exception("Password must include lower case")
    elif not re.search("[A-Z]", passwd):
        raise Exception("Password must include upper case")
    elif not re.search("[0-9]", passwd):
        raise Exception("Password must include number")
    elif not re.search("[_@$]", passwd):
        raise Exception("Password must include alphanumeric character")
    elif not re.search("[\s]", passwd): # For space
        raise Exception("Password must not include space")
    else:
        print("Your password is valid")

password = input("Please enter a password: ")

try:
    check_passwd(password)
except Exception as ex:
    print(ex)
else:
    print("Valid password: else")
finally:
    print("Validation completed")
    print(blank)

##############################################################################################################

# class Person:
#     def __init__(self, name, year):
#         self.year = year
#         if len(name) > 10:
#             raise Exception("Name has invalid lenght")
#         else:
#             self.name = name
# p = Person("Alice", 1989)
# p_1 = Person("MadHatterrrr",1989)
# print(blank)

##############################################################################################################

# Example 1: Working with error handling

who_list = ["1", "2", "5a", "10b", "abc"]
import re

# 1 - Find numerical elements inside who_list
print("Question 1")

for x in who_list:
    try:
        rslt = int(x)
        print(rslt)
    except ValueError:
        continue
print(blank)
  
##############################################################################################################

# 2 - Unless user enters "q" value except every value as numerical else print error message.
print("Question 2")

def q(input):
    if re.search("[q]", input):
        raise Exception("Invalid character q !!!")
    else: 
        print("Input is valid")

try:
    user = input("Please enter a value: ")
    q(user)
except Exception as ex:
    print(ex)
finally:
    print("Validation completed")
    print(blank)

##############################################################################################################

# 3 - If password includes Turkish character print error message.
print("Question 3")

def tr(pswd):
    if re.search("[ğ,ü,ş,ı,ö,ç,İ]", pswd):
        raise Exception("Password cannot include Turkish characters!!!")
    else:
        print("Valid password")

try:
    psw = input("Please enter your password: ")
    tr(psw)
except Exception as ex:
    print(ex)
finally:
    print("Validation completed")
    print(blank)

##############################################################################################################

# 4 - Form a factorial function and print error messages according to input.
print("Question 4")
import math

def fct(fc):
    fact = 1
    fc = int(fc)
    if fc < 0:
        raise ValueError("Negative number!!!")

    for i in range(1, fc+1):
        fact *= i
    print(f"Factorial of {fc} is {fact}")

try: 
    fac = input("Please enter a number: ")
    fct(fac)
except Exception as ex:
    print(ex)
finally:
    print("Calculation set")
