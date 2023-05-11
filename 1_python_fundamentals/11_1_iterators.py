# BTK Academy
# Advanced Python Programming From Zero
# Lecture 11.1: Iterators in Python 
# python 11_1_iterators.py
blank = "----------------------"

# Iterators
# An iterator is an object that contains a countable number of values. 
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# For example for loop can be an iterator that can traverse through all the values within given condition.

lst = [1,2,3,4,5]

iterator = iter(lst)
print(iterator) # <list_iterator object at 0x000002A0B5DE90A0>
print(blank)

# Behind for loop
# print(next(iterator)) # 1
# print(next(iterator)) # 2
# print(next(iterator)) # 3
# print(next(iterator)) # 4
# print(next(iterator)) # 5
# print(blank)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
print(blank)

class Numbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = Numbers(10,20) # list is an iterable object
new_iter = iter(list)

while True:
    try:
        elmnt = next(new_iter)
        print(elmnt)
    except StopIteration:
        break
print(blank)

# for i in list:
#     print(i)
