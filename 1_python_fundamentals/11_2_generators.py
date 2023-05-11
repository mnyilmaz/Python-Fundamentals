# BTK Academy
# Advanced Python Programming From Zero
# Lecture 11.2: Generators in Python 
# python 11_2_generators.py
blank = "----------------------"

# Generators
# A generator is a special type of function which does not return a single value, instead, 
# it returns an iterator object with a sequence of values. In a generator function, a yield 
# statement is used rather than a return statement.
# Generates an spaceless iterator. Doesn't consume memory.

# That process isn't threatening the memory at this stage but in further applications that'll be a problem.
# def cube():
#     result = []
#     for i in range(5):
#         result.append(i**3)
#     return result
# print(cube())

# Non Generator Form
# list = [i**3 for i in range(5)]
# print(list)

# Generator Form (as object, next method or try-except must be added)
# list = (i**3 for i in range(5))
# print(list)

# Instead of that opeariton we'll be using Generators to save memory

def cube():
    for i in range(10):
        yield i**3 # with yield keyword element won't be stored just printed

print(cube()) # <generator object cube at 0x000001F6518EDF20>

# generator = cube()
# iterator = iter(generator)
iterator = cube()

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break


print(blank)

