# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.6: Loops in Pyhton - Loop Examples - Prime Number Determination
# python 4_6_prime_number.py
blank = "----------------------"

# Prime Number Determination

"""
RULES:
# 1 : Try to find if given number is prime or not.
"""

number = int(input("Please enter a number: "))
is_prime = False

if number > 1:
    for i in range(2,number):
        if number % i == 0:
            is_prime = True
            break
      
if is_prime:
    print(f"{number} is not a prime number.")
else:
    print(f"{number} is a prime number.")
