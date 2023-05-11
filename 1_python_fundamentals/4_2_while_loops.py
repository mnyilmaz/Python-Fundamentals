# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.2: Loops in Pyhton - While Loops
# python 4_2_while_loops.py
blank = "----------------------"

# While Loop
x = 0

while x <= 100:
    # if x % 2 == 0:
    #     print(f"{x} is an even number.")
    # else:
    #     print(f"{x} is an odd number.")
    x+=1       
print("Cycle has ended.")
print(blank)

name = "" # Considered as False

while not name.strip(): # It wil continue until user enter a name and strip prevents spaces
    name = input("Please enter your name: ")
print(blank)

##############################################################################################################

# Example 1 :  Working with while loops

nums = [1, 3, 5, 7, 9, 12, 19, 21]

# 1 - Print all the elements in nums using while.
i = 0
while  (i < len(nums)):
    print(nums[i])
    i +=1
    if i > len(nums):
        break
print(blank)

##############################################################################################################

# 2 - Get first and last element from the user and print all the odd numbers between.
start = int(input("Please enter the first value: "))
end = int(input("Please enter the last value: "))
nums.insert(0,start)
nums.insert(9, end)

j = 0
while j < len(nums):
    if nums[j] % 2 != 0:
        print(f"{nums[j]} is an odd number.")
    j+=1
print(blank)

##############################################################################################################

# 3 - Print numbers between 1-100 as decreasing.
y = 100
while y >= 1:
    print(y)
    y-=1
print(blank)

##############################################################################################################

# 4 - The 5 numbers to be received from the user will be printed in sequence.
numbers = []
z = 0
while z < 5:
    n = int(input(f"Please enter the {z+1}. number: "))
    numbers.append(n)
    
    z+=1
numbers.sort()
print(f"Sorted list is = {numbers}")

print(blank)

##############################################################################################################

# 5 - Unlimited product information will be obtained from the user, kept in a list.
# Amount of product must be received from user.
# List form must be as dictionary.
# After user finished defining the products, they must be printed in while loop.
print(blank)

products = []
a = 0
amount = int(input("Please enter the amount of products: "))
print(blank)

while a < amount:
    name = input("Enter the name of the product: ")
    price = int(input("Enter the price of the product: "))
    products.append({
        'name' : name,
        'price' : price
    })
    a += 1
print(blank)

for product in products:
    print(f"Product: {product['name']}\nProduct price: {product['price']}  ")
