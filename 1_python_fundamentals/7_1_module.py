# BTK Academy
# Advanced Python Programming From Zero
# Lecture 7.1: Module in Python
# python 7_1_module.py
blank = "----------------------"

# Modules
# In simple terms, we can consider a module to be the same as a code library or a file that 
# contains a set of functions that you want to include in your application.
# to install: pip install package_name


# math.py Module Usage
# Method 1 
import math # as process

result = dir(math)
# print(result) # this will print all the functions that math.py module require
# value = help(math) # this will print detailed documentation
print(blank)

sqrt = math.sqrt(44)
factor = math.factorial(9)
floor = math.floor(4.9)
ceiling = math.ceil(4.9)
# process = process.log(6) -> if we add as after importing added keyword may used as math

##############################################################################################################

# Method 2 
from math import * # importing desired methods or all with *
value_2 = log(5) # math.log is not required for this method
value_3 = factorial(45)
print(value_2)
print(value_3)

# The last defined function is detected after import.
# If we add log function below import program will use the latest function.
print(blank)

##############################################################################################################

# random.py Usage
import random

rnd = random.random() # 0.0 - 1.0 random nunber interval
uni = random.uniform(1,10) # random numbers between 1 - 10 (programmer can define interval)
list = ["alice", "hatter", "chess", "absolem"]
rndlist = list[random.randint(0,len(list)-1)]
rndch = random.choice(list)
numlist = range(100)
rndsmp = random.sample(numlist,6) # brings 6 sample from given list
print(rndlist)
print(rndch)
print(rndsmp) # type is list
random.shuffle(list) # shuffles list
print(blank)

##############################################################################################################

# mod.py Usage
import _mod_1
rslt = dir(_mod_1)
print(rslt)

fnc = _mod_1.func(3)
print(fnc)

p = _mod_1.Person()
p.speak()
