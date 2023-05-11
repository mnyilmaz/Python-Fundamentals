# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.3: Loops in Pyhton - While Loops
# python 4_3_break_cnt_methods.py
blank = "----------------------"

# Break and Continiue
name = "Alice"

for letter in name:
    if letter == "i":
        break # Stops the loop immediately when letter "i" occurs in string
    print(letter)
print(blank)

for letter in name:
    if letter == "c": 
        continue # Continues the loop but ignoring the letter "c" while printing like passing
    print(letter)
print(blank)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
print(blank)

##############################################################################################################

# Practice 1: Print sum of odd numbers between 1-100.
a = 0
sum = 0
while a <= 100:
    a += 1
    if a % 2 == 0:
        continue
    sum += a
print(f"Sum = {sum}")
print(blank)

##############################################################################################################

# Loop Methods
# Range Method
list_1 = [1, 2, 3]

for item in range(50, 100, 10):  # defines a range for the loop  # range(start, stop, step)
    print(item) 
print(list(range(50, 100, 10)))
print(blank)

##############################################################################################################

# Enumerate Method
beginning = "A new beginning"

# index = 0
# for letter in beginning:
#     print(f"Index: {index} Letter: {letter} ")
#     index += 1

for index, letter in enumerate(beginning):
    print(f"Index: {index} Letter: {letter} ") # This method allows to save lines from the code
print(blank)

##############################################################################################################

# Zip Method
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]

# If you need to make match between lists zip method is quite useful for that purpose
print(list(zip(a,b)))
print(blank)

for item in zip(a,b):
    print(item)
print(blank)
