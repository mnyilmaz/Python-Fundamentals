# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.4: Data Identification - Lists
# python 1_4_lists.py
blank = "----------------------"

my_list = [1, 2, 3]
print(my_list)

list_e = ['one', 'two', 'three']
list_g = ['eins', 'zwei', 'drei']
numbers = list_e + list_g
print(numbers)
print(numbers[4])
print(len(numbers))

user_A = ['Alice', 22]
user_B = ['Bob', 27]
users = [user_A, user_B]
print(users) # may print as users[0] or users[1]
print(users[0][0]) # first index's first index

print(blank)

##############################################################################################################

# Example 1: Working with lists

# 1 - Form a list that includes "Alice, Hatter, Chess, Time".
wonderland = ['Alice', 'Hatter', 'Chess', 'Time']
print(blank)

##############################################################################################################

# 2 - How many elements does the formed list have?
print(len(wonderland))
print(blank)

##############################################################################################################

# 3 - What is the first and last element of this list?
print('First element is: ', wonderland[0], 'and last element is: ', wonderland[3])
print(blank)

##############################################################################################################

# 4 - Change 'Time' with 'Absolem'.
wonderland[3] = 'Absolem'
print(wonderland)
print(blank)

##############################################################################################################

# 5 - Is 'Hatter' an element of this list?
print(wonderland.__contains__('Hatter')) # or 'Hatter' in wonderland
print(blank)

##############################################################################################################

# 6 - Print value at -2.
print(wonderland[-2])
print(blank)

##############################################################################################################

# 7 - Get first three element of this list.
print(wonderland[0:3])
print(blank)

##############################################################################################################

# 8 - Change last two elements with 'Rabbit' and 'Caterpiller'.
wonderland[2] = 'Rabbit'
wonderland[3] = 'Caterpiller'
print(wonderland)  # or wonderland[-2:] = ['Rabbit', 'Caterpiller']
print(blank)

##############################################################################################################

# 9 - Add 'Absolem' and 'Chess' into the list.
wonderland.append('Absolem') 
wonderland.append('Chess')
print(wonderland)   # or wonderland = wonderland + ['Absolem', 'Chess']
print(blank)

##############################################################################################################

# 10 - Delete last element of this list.
del wonderland[5]
print(wonderland)
print(blank)

##############################################################################################################

# 11 - Print 'wonderland' list in reverse.
wonderland.reverse()
print(wonderland)  # or wonderland[::-1]
print(blank)

##############################################################################################################

# 12 - Keep the given datas in a list.
'''
s_1 = Alice Kingsleigh 2000, (70,60,70)
s_2 = Chess the Cat 2001, (80,80,70)
s_3 = Absolem the Butterfly 1995, (80,70,90)
'''
s_1 = ['Alice Kingsleigh', 2000, [70,60,70]]
s_2 = ['Chess the Cat', 2001, [80,80,70]]
s_3 = ['Absolem the Butterfly', 1995, [80,70,90]]

underland = [s_1, s_2, s_3]
print(f"{s_1[0]} is {2022 - s_1[1]} years old and her average power is {(s_1[2][0] + s_1[2][1] + s_1[2][2])/3}")
print(blank)

##############################################################################################################

# List Methods

numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
min(numbers) # min value of the list
max(numbers) # max value of the list

val_split = letters[3:6]
print(val_split)

letters.append('h') # adds given element at the end of the list
numbers.insert(5, 7) # first value is representing index which means add 7 to fifth location
numbers.insert(-1, 99) # adds element at the end of the list
numbers.pop() # removes last element from list 
numbers.pop(3) # removes 3rd index
numbers.remove(1) # removes given element from the list
numbers.sort() # sorts elements according to number or alphabet
numbers.reverse() # to reverse list
numbers.count(10) # how many 10 in a list
numbers.clear() # clears list

print(blank)

##############################################################################################################

# Example 2: Working with list methods

names = ['Alice','Hatter','Chess','Absolem']
years = [2000, 1984, 2001, 1995]

# 1 - Add 'White Rabbit' at the end of the list.
names.append('White Rabbit')
print(names)
print(blank)

##############################################################################################################

# 2 - Add 'Caterpiller' at the beginning of the list.
names.insert(0, 'Caterpiller')
print(names)
print(blank)

##############################################################################################################

# 3 - Delete 'Caterpiller' from the list.
names.remove('Caterpiller')
print(names)
print(blank)

##############################################################################################################

# 4 - Get index number of 'Chess'.
print(names.index('Chess'))
print(blank)

##############################################################################################################

# 5 - Is 'Hatter' on the list?
print(names.__contains__('Hatter'))
print(blank)

##############################################################################################################

# 6 - Revers them all!
names.reverse()
print(names)
print(blank)

##############################################################################################################

# 7 - Sort 'names' list into alphabetical order.
names.sort()
print(names)
print(blank)

##############################################################################################################

# 8 - Sort 'years' list.
years.sort()
print(years)
print(blank)

##############################################################################################################

# 9 - Turn jrny = seperate ways,worlds apart into a list.
jrny = 'seperate ways,worlds apart'
here = jrny.split(',')
print(here)
print(blank)

##############################################################################################################

# 9 - What is the max value of 'years'?
max = max(years)
print(max)
print(blank)

##############################################################################################################

# 10 - How many '1995' are there in 'years' list?
print(years.count(1995))

##############################################################################################################

# 11 - Delete all the elements in 'years'.
years.clear()
print(years)
print(blank)

##############################################################################################################

# 12 - Complete 'Seperate Ways' with the inputs from user and keep them in a list.
worlds_apart = []

jrny_1 = input("Someday " )
worlds_apart.append(jrny_1)

jrny_2 = input("Break those chains " )
worlds_apart.append(jrny_2)

jrny_3 = input("One night " )
worlds_apart.append(jrny_3)

print(worlds_apart)
print(blank)

##############################################################################################################

# Tuples
list = [1, 2, 3]
tuple = 1, 2, 3

print("Type of 'list' is: ", type(list))
print("Type of 'tuple' is: ", type(tuple))

print(tuple[2])
print(len(tuple))

# Difference between list and tuple, while list can be modified tuple cannot be. 
# Change is not allowed for tuple type of list. 
# You may store only unchangeble variables in tuples.

# Methods for tuples
tuple.count() # same method with list
tuple.index() # same method with list