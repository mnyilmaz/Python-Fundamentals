# BTK Academy
# Advanced Python Programming From Zero
# Lecture 10.1: Nested Functions in Python 
# python 10_1_nested_functions.py
blank = "----------------------"

def greeting(name):
    print("Hello", name)

greeting("Alice")
print(blank)

# Adresses will be the same
# say_hello = greeting
# print(say_hello)
# print(greeting)

##############################################################################################################

# Encapsulation
def outer(num_1):
    print("outer")
    def inner_increment(num_1):
        print("inner")
        return num_1 + 1
    num_2 = inner_increment(num_1)
    print(f"Number 1 is {num_1} and increment of it is {num_2}")

outer(20)
print(blank)

##############################################################################################################

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if not number >= 0:
        raise ValueError("Number must be positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

try:
    num = int(input("Please enter a number for factorial function: "))
    print(f"Factorial of {num} is {factorial(num)}")
    print(blank)
except Exception as ex:
    print(ex)

##############################################################################################################

# Returning Function from a Function

def power(num):
    def inner(pow):
        return num ** pow
    return inner

two = power(2)
print(two(5)) # result is 2^5 = 32

three = power(3)
print(three(6)) # result is 3^6 = 729
print(blank)

##############################################################################################################

def question_authority(page):
    def inner(role):
        if role == "admin":
            return "Role {0} can acces {1} page".format(role,page)
        else: 
            return "Role {0} cannot acces {1} page".format(role,page)
    return inner

user_1 = question_authority("Product Edit")
print(user_1("admin"))

user_2 = question_authority("Product Edit")
print(user_2("user"))
print(blank)

##############################################################################################################

def process(p_name):
    def sum(*args):
        sum = 0
        for i in args:
            sum+=i
        return sum

    def subtraction(*args):
        sub = 0
        for i in args:
            sub-=i
        return sub

    def multiplication(*args):
        mult = 1
        for i in args:
            mult*=i
        return mult

    def divison(*args):
        div = 1
        for i in args:
            div/=i
        return div

    if p_name == "sum":
        return sum

    elif p_name == "sub":
         return subtraction 

    elif p_name == "multiply":
        return multiplication 

    elif p_name == "divide":
         return divison

sum = process("sum")
sub = process("sub")
mlt = process("multiply")
div = process("divide")

print(f"Sum is = {sum(3,4,5,6)}")
print(f"Substitution is = {sub(3,4,5,6)}")
print(f"Multiplication is = {mlt(3,4,5,6)}")
print(f"Divison is = {div(3,4,5,6)}")
print(blank)

##############################################################################################################

# Function as Parameters

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mlt(a,b):
    return a*b
def div(a,b):
    return a/b

def m(f1, f2, f3, f4, p_name):
    if p_name == "sum":
        print(f1(2,3))
    elif p_name == "sub":
        print(f2(4,5)) 
    elif p_name == "multiply":
        print(f3(6,7)) 
    elif p_name == "divide":
        print(f4(8,9))
    else:
        print("Invalid process")

m(sum, sub, mlt, div, "sum")
m(sum, sub, mlt, div, "sub")
m(sum, sub, mlt, div, "multiply")
m(sum, sub, mlt, div, "divide")
m(sum, sub, mlt, div, "null")
print(blank)

##############################################################################################################

# Decorator Functions
# A decorator in Python is a function that takes another function as its argument, and returns yet another function. 
# Decorators can be extremely useful as they allow the extension of an existing function, without any modification 
# to the original function source code.

def decorator(func):
    def wrapper():
        print("Processes before function")
        func()
        print("Processes after function")
    return wrapper

@decorator # driver = decorator(driver)
def driver():
    print("Charles Leclerc")
driver() # driver()

print(blank)

@decorator # team = decorator(team)
def team():
    print("Scuderia Ferrari")
team() # team()
print(blank)

##############################################################################################################
import math, time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print(f"{func.__name__} Function has completed in {finish-start} seconds")
    return inner

@calculate_time
def pwr(a,b):
    print(f"{a} power {b} is = {math.pow(a,b)}")

@calculate_time
def fctrl(num):
    print(f"Factorial of {num} is = {math.factorial(num)}")

pwr(3,4)
print(blank)
fctrl(8)



