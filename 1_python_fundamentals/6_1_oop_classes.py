# BTK Academy
# Advanced Python Programming From Zero
# Lecture 6.1: Object Oriented Programming in Python - Classes
# python 6_1_oop_classes.py
blank = "----------------------"

# Class
# A class is a code template for creating objects. For example lists are class.

list_obj = [1,2,3] # this object's class is "list"
list_obj.extend([4,5,6,7])

result = type(list_obj)
print(result)
print(list_obj)
print(blank)

# To form a class we may define Person(name, surname, birthday, calculate_age())
# and from this class user can form an object or instance. Classes may include methods.
# Class names must be begin with upper case letter.

# Forming a class
class Wonderland:
    pass
    # define class attributes
    adress = "Underland behind Wonderland"

    # constructor (is a special function that creates an instance of the class)
    def __init__(self, name, madness_level): # self represents an object derived from class
        # define object attributes 
        self.name = name
        self.madness_level = madness_level
        print("__init__ method is working")
     
    # define methods (instance method)
    def intro(self):
        print(f"Hello There! I am {self.name}")
    
    def calculate_madness(self):
        print(f"Total madness is {1234 - self.madness_level}")

##############################################################################################################

# Forming an object or instance
o_1 = Wonderland("Alice", 8)
print(type(o_1))
print(blank)

# Updating
o_1.name = "Mad Hatter"

# Method
o_1.intro()
o_1.calculate_madness()

# Accessing Object Attributes
print(f"Name: {o_1.name}\nMadness Level: {o_1.madness_level}\nAdress: {o_1.adress}")
print(blank)

##############################################################################################################

# Practice
class Circle():
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2*self.pi*self.radius
    
    def area(self):
        return self.pi*(self.radius**2)

circle = Circle(9)
print(f"Radius of a circle is: {circle.radius}\nPerimeter is: {circle.perimeter()}\nArea is: {circle.area()}")
