# THK_Python_Bootcamp_Day_3
# NOTES
# Index error: If index that we're trying to define does not exist that will give us an ındex error.
# Type error: Sum of two different variables error such as int + string
# You can convert sum of int and string as str(list1[0]) + str(list2[0])
# If it is not int I suppose it is calculating its char value which is ASCII code
# Append method adding a new value at the end of our list

# List-Array Structure

# Printing an array
a = ["Nathan", "Sam", 123456, 789101, 4.00, 3.35, 'Tarih', 'Arkeoloji']
# print(a)
for i in a:
   # print(i, "\n")
     print(i)
print(a[1])

# Two arrays in a line
list1, list2 = ["Lara", "Croft", "Tomb", "Raider"], ["The", "Last", "Of", "Us"]
for q in list1:
    if q == 1:
        break
print(q)

for t in list2:
    if t == 2:
        break
print(t)

# Sum of two elements of different arrays
list3 = list1[0] + list2[0]
print(list3)

# Printing char by char
list3 = 'Moonlight'
for r in list3:
    print(r)

# Slicing arrays - q:t includes q index but not including t index
b = a[1:4]
print(b)

# Append method

# Make an array that user will determine its length and indexes will be selecting by user
listUser = []
lngth = int(input("Please enter the length of listUser array = "))

# for h in range(lngth): // used while because we wanted to determine indexes on the list
h = 0
while h<lngth:
    indx = int(input("Please enter index for listUser array = "))
    if indx not in listUser:
        listUser.append(indx)
        h+=1
    else:
        print("The index you're trying to enter is already in the list")
    print(listUser)

print("Whole list is down below: ")
print(listUser)

# Deleting list
del listUser[3]
print("New form of the list: ", listUser)

# Inserting new value into the list
listUser.insert(3, 96)
print("New value inserted list: ", listUser)

# Printing max value of the list
print("Max value of the list: ", max(listUser))

# Printing min value of the list
print("Min value of the list: ", min(listUser))

# Original list
listUser.sort(reverse=False)
print("Original list: ", listUser)

# Reverted list - Sorting
listUser.sort(reverse=True)
print("Reversed list: ", listUser)

# Reverting list with another method - Not sorting
print("Not sorted reverted list: ", listUser[::-1])
