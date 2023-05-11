# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.4: Loops in Pyhton - List Comprehensions
# python 4_4_list_comprehensions.py
blank = "----------------------"

# List Comprehensions

# nums = []
# for x in range(10):
#     nums.append(x)
# print(nums)

numbers = [x for x in range(10)] # print numbers 0-9
print(numbers)

print(blank)

##############################################################################################################

# Take square of numbers only multiple of 3
sqr = [x**2 for x in range(10) if x % 3 == 0] 
print(sqr)

print(blank)

##############################################################################################################

# Print every character of given string
str = "Wonderland"
# lst = []
# for letter in str:
#     lst.append(letter)
# print(lst)

lststr = [letter for letter in str]
print(lststr)

print(blank)

##############################################################################################################

# Print ages according to given years below
years = [1995, 2000, 2001, 2021]
ages = [2022-year for year in years]
print(ages)

print(blank)

##############################################################################################################

# Print even numbers
results = [x if x % 2 == 0 else "Odd" for x in range(1, 10)]
print(results)

print(blank)

##############################################################################################################

# Loop inside loop

# result = []

# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)

result = [(x,y) for x in range(3) for y in range(3)]
print(result)