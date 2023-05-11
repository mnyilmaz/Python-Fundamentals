# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.6: Data Identification - Sets, Values and References
# python 1_6_sets_value_reference.py
blank = "----------------------"

# Sets (type of list)
journey = {'someday', 'love', 'will', 'find', 'you'}
print(journey)
print(blank)

# Cannot be indexed 
# Cannot be sorted

for x in journey:
    print(x)
print(blank)

journey.add('break')
journey.update(['those', 'chains', 'that', 'bind', 'you'])
journey.add('someday') # if this data is already in list set won't add it again
journey.add('worlds apart')
journey.remove('worlds apart') # or .discard()
journey.pop()
print(journey)
journey.clear()
print(blank)

##############################################################################################################

# Value Types --> int, str
# Differences cannot effect the others
x = 5
y = 25

x = y
y = 10
print(x) # value of x won't be 10 because y's value changed after x = y
print(blank)

##############################################################################################################

# Reference Types --> lists, class
# Differences can effect the others
a = ['alice', 'rabbit', 'hatter']
b = ['alice', 'rabbit', 'hatter']

a = b # address's are equal from now on so any change's on a or b will effect them both
b[1] = 'absolem'
print(a,b) # 'absolem' will appear on both list because they carry the same address