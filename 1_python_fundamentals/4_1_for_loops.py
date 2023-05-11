# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.1: Loops in Pyhton - For Loops
# python 4_1_for_loops.py
from math import prod
blank = "----------------------"

# For Loops
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num) # This loop prints every element that number includes
# If you change print(x) as print("Hello") result will print hello for amount of numbers
print(blank)

names = ["alice", "hatter", "absolem"]
for name in names:
    print(f"My name is {name}") # This loop prints every name with the given sentence
print(blank)

name = "Mad Hatter"
for n in name:
    print(n) # This loop prints every string character that given in name
print(blank)

tuple = ([1,2], [3,4], [5,6], [7,8])
for a,b in tuple:
    print(a) # prints only first element of every tuple element
    print(b) # prints only second element of every tuple element
    print(a, b)
print(blank)

dic = {"a" : 1, "b" : 2, "c" : 3}
for d in dic:
    print(d) # prints keys "a", "b" and "c"
print(blank)

for key, value in dic.items():
    print(key, value) # prints keys and values
print(blank)

##############################################################################################################

# Example 1 : Working with for loops
nums = [1, 3, 5, 7, 9, 12, 19, 21]
instruments = ["piano", "violin", "guitar", "drum"]

##############################################################################################################

# 1 - Which numbers are multiple of 3?
for n in nums:
    if n % 3 == 0:
        print(f"{n} is multiple of three.")
print(blank)

##############################################################################################################

# 2 - What is the sum of elements in nums?
sum = 0
for n in nums:
    sum += n
print(f"Sum of these elements is = {sum}")
print(blank)

##############################################################################################################

# 3 - Take square of odd numbers in nums list.
for n in nums:
    if n % 2 != 0:
        sqr = n ** 2
        print(f"Square of {n} is {sqr} ")
print(blank)
     
##############################################################################################################

# 4 - Which instruments are have at most 5 characters?
for ins in instruments:
    len_in = len(ins)
    if len_in <= 5:
        print(f"{ins} has {len_in} characters.")
print(blank)

##############################################################################################################

# 5 - What is the sum of products?
products = [
    {"name": "iPhone 7", "price" : "4000"},
    {"name": "iPhone 8", "price" : "5000"},
    {"name": "iPhone SE", "price" : "5500"},
    {"name": "iPhone 10", "price" : "7000"},
    {"name": "iPhone 11", "price" : "9000"}
]

pro_sum = 0
for p in products:
    pro_sum += int(p["price"])
    print(p)
  # print(p["name"])
  # print(p["price"])

print(f"Sum of these products is = {pro_sum}")
print(blank)

##############################################################################################################

# 6 - Print products that their values ar at most 5000.
for p in products:
    if int(p["price"]) <= 5000:
        print(p["name"], "is", p["price"], "TL")


