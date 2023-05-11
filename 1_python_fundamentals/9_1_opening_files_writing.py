# BTK Academy
# Advanced Python Programming From Zero
# Lecture 9.1: File Extension in Python - Opening Files & Writing
# python 9_1_opening_files_writing.py
from os import remove


blank = "----------------------"


# open() function is used to open files. 
# To use open() function: open(file_name, file_access_mode)
# file_access_mode -> defines purpose of file opening


# "w" : (Write) Writing mode. Forms file at the location.
# always updates content inside file, never stores older contents

wrt = open("write_file.txt","w", encoding = "utf-8") # adding Turkish characters
wrt.write("Alice in Wonderland") # writing inside file
wrt.close() # closing the file otherwise file may consume resources while open 
#file = open("C:/Users/Ahmet&MerveNur/Desktop/new_file.txt","w") # Forms file at the given location
# print(wrt)

##############################################################################################################

# "a" : (Append) Appending mode. Forms file if file is not at the location.

apnd = open("append_file.txt","a", encoding = "utf-8") 
apnd.write("\nAlice in Wonderland")
apnd.close()

##############################################################################################################

# "x" : (Create) Creating mode. Gives error if file exist.

crt = open("create_file.txt","x", encoding = "utf-8") 
crt.close()
crt = remove("create_file.txt") # to prevent error while coding

##############################################################################################################

# "r" : (Read) Reading mode. If file is not at the location gives error.

try:
    rd = open("append_file.txt","r") # default mode is "r" 
    print(rd)
except FileNotFoundError:
    print("File not found")
finally:
    rd.close()
    print("File has been closed")
    print(blank)

# Read with for loop  
rd_2 = open("append_file.txt","r", encoding = "utf-8") 
# for i in rd_2:
#     print(i, end="")
# print(blank)

# Read with read method
include = rd_2.read()
print(include)
rd_2.close()
print(blank)

# Reading by size
rd_2 = open("append_file.txt","r", encoding = "utf-8") 
print(rd_2.read(6)) # reads first 6 characters only
rd_2.close()
print(blank)

# readline() Function
# This functions reads only lines
rd_2 = open("append_file.txt","r", encoding = "utf-8") 
print(rd_2.readline(), end="")
rd_2.close()
print(blank)

# readlines() Function
# This functions reads as list
rd_2 = open("append_file.txt","r", encoding = "utf-8") 
rd_list = rd_2.readlines()
print(rd_list)
print(blank)
print(f"Type of rd_list is: {type(rd_list)}")
rd_2.close()
print(blank)

# Using "with"
with open("new_file.txt", "r", encoding="utf-8") as fl:
    content = fl.read()
    print(content)
    print(f"Cursor is at {fl.tell()}. byte") # will tell the exact location of cursor
    fl.seek(18) # print after 18. byte
    content_2 = fl.read()
    print(content_2)
print(blank)
# With "with" command file will close automatically

##############################################################################################################

# Updating with files
# Update selected byte
with open("new_file.txt", "r+", encoding="utf-8") as file:
    file.seek(20)
    file.write("trytrytry")

with open("new_file.txt", "r+", encoding="utf-8") as file:
    print(file.read())
print(blank)

# Update at end of the file 
with open("new_file.txt", "a", encoding="utf-8") as fll:
    fll.write("\ntrytrytry")

with open("new_file.txt", "r", encoding="utf-8") as fll:
    print(fll.read())
print(blank)

# Update at start of the file 
with open("new_file.txt", "r+", encoding="utf-8") as fle:
    cnt = fle.read()
    cnt = "trytrytry\n" + cnt 
    fle.seek(0)
    fle.write(cnt)
    print(cnt) 

with open("new_file.txt", "r", encoding="utf-8") as fle:
    print(fle.read())
print(blank)

# Update at middle of the file 
with open("new_file.txt", "r+", encoding="utf-8") as f:
    file_list = f.readlines()
    middle = file_list.insert(1, "trytrytry\n")
    f.seek(0)
    f.writelines(file_list)
    for i in file_list:
        f.write(i)

with open("new_file.txt", "r", encoding="utf-8") as f:
    print(f.read())
print(blank)