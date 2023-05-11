# BTK Academy
# Advanced Python Programming From Zero
# Lecture 5.2: Methods in Pyhton - Lambda Expressions, Map and Filter
# python 5_2_lambda_map_filter.py
blank = "----------------------"

# Map Method

def sqr(num): return num ** 2

numbers = [1,2,3,4,5]
sqrs = []

# The map function takes each item in a given iterable and includes all of them in a new lazy iterable, 
# transforming each item along the way.
# def map(function, iterable):
    # return (function(x) for x in iterable)

# in map method only func name is given its sqr not sqr()
for item in map(sqr, numbers): 
    sqrs.append(item)
print(sqrs)

print(blank)

##############################################################################################################

# Anonymous Method - Lambda Expression
# Sometime in loops or processes user wouldn't need methods or functions as sqr all the time.
# For that we may defien anonymous functions for single useage.

square = lambda num: num **2 # may use as square(number) will work same as the function
print(list(map(square, numbers)))

print(blank)

##############################################################################################################

# Filter Function
# The filter function doesn't transform the items, 
# but it's selectively picks out which items it should include in the new lazy iterable.
# def filter(function, iterable):
#     return (x for x in iterable if function(x))

check_even = lambda num: num % 2 == 0 # def check_even(num): return num % 2 == 0
r = list(filter(check_even, numbers))
print(r)

print(blank)

##############################################################################################################

# Scope in Python: Local and Global Variables
# global scope
x = "global x"

# local scope
def function():
    x = "local x"
    print(x)

# Changes inside a function don't effect variables outside function. That's the reason result below.
function() # local x will be printed
print(x) # global x will be printed

print(blank)

##############################################################################################################

name = "Alice"

def change_name(new_name):
    name = new_name
    print(name)

change_name("Hatter") # Hatter
print(name) # Alice

print(blank)

##############################################################################################################

str = "Wonderland"

def won():
   # str = "Alice"
   
    def und():
        #str = "Hatter"
        print("This is " + str) # This is Wonderland
    
    und() # This is Hatter

won()
print(str) # Wonderland

print(blank)

##############################################################################################################

a = 50
def test():
    global a
    print(f"a is {a}") # is 50

    a = 100
    print(f"a has changed into {a}") # into 100

test()
print(a) # 100