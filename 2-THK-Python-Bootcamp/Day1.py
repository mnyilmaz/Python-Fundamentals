# THK_Python_Bootcamp_Day_1
# NOTES
# Python is an object oriented programming language

print('Hello World!')
print("Hello World!")
print(7)
print(7+4)
print('7+4')

# print('5'+ 9) --> type error

# Sum of two variables
x = 5
y = 6
z = x+y
print('z =', z)

# Get data from user
a = int(input("Please enter a value for a "))
b = int(input("Please enter a value for b "))
# c = int(a) + int(b) --> value error
c = a+b
print('c =', c)

# Determine max number that you get from user
if a > b:
    print("Max number is a = ", a)
elif a == b:
    print("Numbers are equal = ", b)
else:
    print("Max number is b = ", b)

# While Loop - Determine max number of these 6
i = 1
maximum = 0

while i <= 3:
    q = int(input("Please enter a value for q "))
    t = int(input("Please enter a value for t "))

    if q > t:
        print("Max number is q = ", q)
        if q > maximum:
            maximum = q

    elif q < t:
        print("Max number is t = ", t)
        if t > maximum:
            maximum = t
    else:
        print("Numbers are equal")
        maximum = q
    i += 1
print("Maximum number of these 6 number is = ", maximum)