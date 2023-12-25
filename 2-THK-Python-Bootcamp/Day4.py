# THK_Python_Bootcamp_Day_4
# NOTES

# Tuple Structure
# Tuples are used to store multiple items in a single variable
# Tuple is ordered and unchangeable so, you cannot add, change or remove item

# Definition of tuple
thistuple = ("python", "Java", "C#", "C++")
print(thistuple)

# If you define new value
thistuple = "C"
print(thistuple)

# Get value by index
thistuple = ("python", "Java", "C#", "C++")
print(thistuple[3])

# Search index in tuple
print(thistuple.index("Java"))

# Tuple data types
tupleStr = ("Drake's Fortune", "Among the Thieves", "Drake's Deception")
tupleInt = (1, 2, 9, 0, 9, 0, 6, 0)
tupleBol = (True, False, True, False)
tupleDif = ("Among the Thieves", 0, 6, False)
print(tupleStr)
print(tupleInt)
print(tupleBol)
print(tupleDif)

# Length of a tuple
print(len(thistuple))

# Search value that comes from user
# We will use thistuple tuple
value = input("Enter the value: ")
value = value.lower()
if value in thistuple:
    print("Value that you're looking for in", thistuple.index(value), "line")
else:
    print("Value that you're looking for is not on the tuple")

# Python Dictionary Structure
# Only values can be processed. Cannot use index numbers for processes.

# Definition of dictionary
thisdict = {
    "brand": "Tesla",
    "electric": True,
    "year": 2021,
    "colors": ["blue", "red", "black"]
}
print(thisdict)
print(thisdict["brand"])
print(thisdict["colors"][2])


# Function Structure
# A function is a code block which only runs when it is called
# You have to define a function with "def" before calling it
# Function is a program by its own

# Definition of function
def myFunction():
    print("This is a function")


myFunction()



# Arguments - can be passed into functions as arguments
def myfunction(fname):
    print(fname + "References")


myfunction("Ragnarok ")
myfunction("A Thief's End ")
myfunction("Last of Us ")


# Another example about functions
def newfunction(value1, value2):
    x = value1
    y = value2
    return x + y
    # or return value1 + value2


value1 = int(input("Please enter the first value: "))
value2 = int(input("Please enter the second value: "))
z = newfunction(value1, value2)
print("Sum of x and y is = ", z)


# Recursion Function
# Which means a defined function can call itself
# Can be used in factorial calculation

# Factorial calculation with recursion functions
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


num = int(input("Please enter a value for factorial function: "))
print("Factorial of", num, "is:", factorial(num))


# Object-Oriented Programming Classes include objects to call them first we have to define class then variables
# inside it All classes have _init_(), which is always executed when the class is being initiated. Use _init_()
# function to assign values to object properties, or other operations that are necessary to do when the object is
# being created.

# Defining a class
class myClass:
    x = 5
    y = 10
    for i in range(x):
        print("Hello class!!!")


# p1 and p2 are objects of myClass class
p1 = myClass()
print(p1.x)
p2 = myClass()
print(p2.y)


# Example about _init_()
class Hogwarts:
    def __init__(self, house, head, student):
        self.house = house
        self.head = head
        self.student = student


h1 = Hogwarts("Slytherin", "Severus Snape", "Draco Malfoy")
print(h1.house)
print(h1.head)
print(h1.student)

h2 = Hogwarts("Gryffindor", "Minerva McGonagall", "Hermione Granger")
print(h2.house)
print(h2.head)
print(h2.student)


# Methods
class Uncharted:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def firstAction(self):
        print("Hello my name is " + self.name + " " + self.surname)


u1 = Uncharted("Nathan", "Drake")
u1.firstAction()
