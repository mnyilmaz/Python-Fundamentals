# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.3: Data Identification - Strings
blank = "----------------------"

name = "Alice" # doesn't matter if you use " or ' while defining a string
surname = "Turing"
age = 27
greeting = "She is" + " " + name + " " + surname + " " + "\nand her age is" + " " + str(age) # \n allows you to get a new line 

print(greeting)
print(greeting[0]) # to get first character of a string
print(len(greeting)) # gives length of a string (in this case result will be 38)
print(greeting[len(greeting) - 1]) # to get last character of a string (length - 1)
print(blank)

print(greeting[2:7]) # start from 2nd index until 7th index
print(greeting[3:]) # start from 3rd chartacter go until last character
print(greeting[:17]) # start from first character but stop when it comes to 17
print(greeting[3:35:2]) # start from 3rd stop when 35th step two by two
print(blank)

##############################################################################################################

# String Formatting

print("She is {} {}".format(name,surname)) # index 0 = name, index 1 = surname
# print("She is {1} {0}".format(name,surname)) --> result will be Turing Alice
# print("She is {n} {s}".format(n = name, s = surname)) --> result will be Alice Turing
print("She is {} {} and her age is {}".format(name,surname,age)) # index 0 = name, index 1 = surname
print(f"She is {name} {surname} and her age is {age}") # f usage is quite easy to integrate values 
print(blank)

result = 200/700
print("The result is {}".format(result))
print("The result is {r:1.3}".format(r = result)) # 1.3 implies that get only first three index after comma for float numbers
print(blank)

##############################################################################################################

# Example 1: Working wiht characters

website = "https://en.wikipedia.org/wiki/Syracusia"
content = "The exact dimension of Syracusia is unknown"

# 1 - How many characters there are inside 'website' ?
print(len(website)) # Ans: 39
print(blank)

##############################################################################################################

# 2 - Only get 'en' from website.
print(website[8:10])
print(blank)

##############################################################################################################

# 3 - Only get 'org' from website.
print(website[21:24])
print(blank)

##############################################################################################################

# 4 - Get first 15 and last 15 characters from 'content'.
f_15 = content[:17] # if you count spaces
l_15 = content[len(content) - 17:] # if you count spaces or [-15:]
print(f_15)
print(l_15)
print(blank)

##############################################################################################################

# 5 - Print all characters in 'content' in reverse.
print(content[::-1])
print(blank)

name_ex, surname_ex, age_ex, job_ex = 'Bob', 'Turing', '27', 'Cryptographer'

##############################################################################################################

# 6 - Print : 'He is Bob Turing, his age is 27 and he is a Cryptographer'.
print(f"He is {name_ex} {surname_ex}, his age is {age_ex} and he is a {job_ex}")
print(blank)

##############################################################################################################

# 7 - Change 'w' with 'W' in expression 'Hello world'
exp_1 = "Hello world"
print(exp_1.replace("w", "W")) # or exp_1 = exp_1[0:6] + 'W' + exp_1[-4:]
print(blank)

##############################################################################################################

# 8 - Print three times expression 'abc'
exp_2 = "abc"
print(exp_2 * 3)
print(blank)

##############################################################################################################

# String Methods

message = "Deep in the dark you think everything's right"
message = message.upper() # Turn every character into upper case
message = message.lower() # Turn every character into lower case
message = message.title() # Converts the first character of each word to upper case
message = message.capitalize() # Capitalize first word's character
message = message.strip() # Returns a trimmed version of the string
message = message.split() # Splits every word in a row if there are spaces
#message = message.split('.') # Splits every word from '.'
message = ' '.join(message) # Combine splitted words with spaces Deepinthedark --> Deep in the dark
message = message.replace('dark','night').replace('right','wrong')
message = message.center(50, '*') 

index = message.find('dark') # This index will turn an int number and this number will represent searched word'S first index number
isFound = message.startswith('e') # Looking for words that start with 'e' 
isFound = message.endswith('p') # Looking for words that end with 'e' 

##############################################################################################################

# Example 2 - Working with methods
h_w = ' Hello World '

# 1 - Remove first and last spaces from ' Hello World '.
print(h_w.strip())
print(blank)

##############################################################################################################

# 2 - Remove every character from 'website' except "Syracusia".
print(website.lstrip('htps:/en.wikpdaorg'))
print(blank)

##############################################################################################################

# 3 - Turn every character into lower case in 'content'.
print(content.lower()) # or .casefold()
print(blank)

##############################################################################################################

# 4 - How many 'a' characters in 'website' ?
print(website.count('a'))
print(blank)

##############################################################################################################

# 5 - Does 'website' start with "www" and end with "org"?
print(website.startswith('wwww'))
print(website.endswith('org'))
print(blank)

##############################################################################################################

# 6 - Is there any ".org" inside 'website'?
print('.org' in website)
print(blank)

##############################################################################################################

# 7 - Every character in 'content' is in alphabetic order?
print(content.isalpha())
print(blank)

##############################################################################################################

# 8 - Align decided expresiion an add * its right and left.
h_w = h_w.center(50, '*')
print(h_w)
print(blank)

##############################################################################################################

# 9 - Change every space with "-" in 'content'.
print(content.replace(' ', '-'))
print(blank)

##############################################################################################################

# 10 - Replace "World" with "There" in 'Hello World'.
print(h_w.replace('World', 'There'))
print(blank)

##############################################################################################################

# 11 - Split every character from their spaces between in 'content'.
print(content.split(' '))