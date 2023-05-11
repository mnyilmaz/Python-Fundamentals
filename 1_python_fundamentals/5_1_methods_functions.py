# BTK Academy
# Advanced Python Programming From Zero
# Lecture 5.1: Methods in Pyhton - Methods and Functions
# python 5_1_methods_functions.py
blank = "----------------------"

# Method
# In Python, a method is a function that is available for a given object because of the object's type.
# Methods are class specific.

l = [1, 2, 3]
l.append(4)
l.pop()
print(l)
print(blank)

str = "wonderland"
str.upper()
print(str)
print(blank)

##############################################################################################################

# Functions
# In Python, a function is a group of related statements that performs a specific task. 
# Functions help break our program into smaller and modular chunks. 
# As our program grows larger and larger, functions make it more organized and manageable. 
# Furthermore, it avoids repetition and makes the code reusable

# Message Printer Function
def say_mad(name = "Alice"):
    # print(f"The Mad {name}")
    return "The Mad" + name

# say_mad("Hatter")
# say_mad()
msg = say_mad(" Hatter")
print(msg)
print(blank)

##############################################################################################################

# Sum Function
def total(x,y):
    return x + y

r = total(564,474)
print(f"Sum = {r}")
print(blank)

##############################################################################################################

# Age Calculation
def age_c(birth_year):
    return 2022 - birth_year

age = age_c(1995)
print(f"Your age is {age}")
print(blank)

##############################################################################################################

# Retirement Age
def ret(b_y, n):
    '''
    DOCSTRING: Calculation of retirement according to your birth year
    INPUT: Birth year
    OUTPUT: Years left for your retirement
    '''
    a = age_c(b_y)
    retirement = 65 - a
    if retirement > 0:
        print(f"{n} will be retired after {retirement} years later.")
    else:
        print(f"{n} is {a} years old and already retired.")

ret(1951,"Alice")
print(blank)
print(help(ret))
print(blank)

##############################################################################################################

# Function Parameters

def change_name(n):
    n = "Alice"

name = "Hatter"
change_name(name)
print(name) # Output will be Hatter
print(blank)

##############################################################################################################

#Slicing
def change(z):
    z[0] = "Japan"

countries = ["New Zealand", "Peru"]
change(countries[:]) # slicing - copies elements into a new list without changing their adress
print(countries)

# c = countries[:] # slicing - copies elements into a new list without changing their adress
# c[0] = "Japan"
# print(countries)
# print(c)
print(blank)

##############################################################################################################

# Using Many Parameters
def add(*params): # in this situation you may able to send parameteres as much as you desire to the function
    # return sum((params))
    sum = 0
    for n in params:
        sum += n
    return sum

result = add(45,34,56,45335,5643,3652,36523,63236,57,56)
print(f"Sum is = {result}")
print(blank)

##############################################################################################################

# Defining MOOOOOOORE Parameters
def display_user(**args): # forms dictionary ay use params instead of args
    for key, value in args.items():
        print("{} is {}".format(key, value))

display_user(user = "Alice", old = 22, place = "Wonderland")
print(blank)
display_user(user = "Hatter", old = 77, place = "Wonderland", job = "Hatter")
print(blank)
display_user(user = "Rabbit", old = 34, place = "Wonderland", job = "TickTock", color = "cotton")
print(blank)

##############################################################################################################

# Displaying arguments
def my_func(s, d, *args, **kwargs):
    print(s) # int
    print(d) # int
    print(args) # tuple not list
    print(kwargs) # dictionary

my_func(10, 20, 30, 40, 50, key_1 = "value 1", key_2 = "value 2")
print(blank)

##############################################################################################################

# Example 1: Working with functions
# 1 - User will determine a word to display and decide how many times word will be printed.
def display(m,n):
    for x in range(n):
            print(m)
            if x == n:
                break

display("Alice", 5)
print(blank)

##############################################################################################################

# 2 - Form a function that can receive unlimited parameters and form a list with these elements.
def unlim(*args):
    list_1 = []
    for arg in args:
        list_1.append(arg)
    return list_1

lim = unlim(34,56,678,8,79,879,78,97,80,87,0)
print(lim)
print(blank)

##############################################################################################################

# 3 - Find all the prime numbers between two given inputs.
def prime(n,d):
    for i in range(n,(d+1)):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                print(i)
prime(1,9)
print(blank)

##############################################################################################################

# 4 - Form a list consist the exact divisors of the given number.

def exact(e):
    ex = []
    for i in range(1, e):
        if e % i == 0:
            ex.append(i)
    print(ex)
    return ex

exact(100)