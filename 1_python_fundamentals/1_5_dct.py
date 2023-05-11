# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.5: Data Identification - Dictionaries
# python 1_5_dct.py
blank = "----------------------"

# Dictionaries work as key - value relationship.
# Like 34 is representig İstanbul.
blank = "\n"

# Key - Value With Lists
countries = ['Japan', 'Australia']
dialing_codes = [81, 61]
print("Japan's dialing code is:", dialing_codes[countries.index('Japan')])

print(blank)

##############################################################################################################

# Using Dictionaries -> dict = {key : value}
dialing_codes = {'Japan' : 81, 'Austrlia' : 61, 'New Zealand' : 64}
print("Tyepe of dialing_codes is:", type(dialing_codes))
print("New Zealand's dialing code is:", dialing_codes['New Zealand'])

# Adding new key to the dictionary
dialing_codes['Peru'] = 52
print(dialing_codes)

# Updating 
dialing_codes['Peru'] = 51
print(dialing_codes)

print(blank)

bonkers = {
    'alice' : {
        'name' : 'Alice Kingsleigh',
        'roles' : ['head', 'mad'],
        'age' : 22, 
        'job' : 'Captain', 
        'living' : 'London' 
        },

    'hatter' : {
        'name' : 'The Mad Hatter',
        'roles' : ['head', 'hatter'],
        'age' : 'unknown', 
        'job' : 'Hatter', 
        'living' : 'Wonderland'
    },

    'chess' : {
        'name' : 'The Cheshire Cat',
        'roles' : ['side', 'clever'],
        'age' : 'unknown', 
        'job' : 'Fraud Detection', 
        'living' : 'in Everywhere'
    }
}

print(bonkers['hatter'])
print(bonkers['chess']['name'])
print(bonkers['alice']['roles'][1])

print(blank)

##############################################################################################################

# Example 1 : Working with dictionaries
dialing = {}

code_1 = input("Please enter the code: ") # 81
c_1 = input("Please enter the country: ") # Japan
r_1 = input("Please enter the region: ") # East Asia
a_1 = input("Please enter the area: ") # 377.975

print(blank)

code_2 = input("Please enter the code: ") # 61
c_2 = input("Please enter the country: ") # Australia
r_2 = input("Please enter the region: ") # Apac
a_2 = input("Please enter the area: ") # 7.688.000

print(blank)

code_3 = input("Please enter the code: ") # 64
c_3 = input("Please enter the country: ") # New Zealand
r_3 = input("Please enter the region: ") # Oceania
a_3 = input("Please enter the area: ") # 268.021


dialing.update({
    code_1 : {
        'country' : c_1,
        'region' : r_1,
        'area' : a_1
    },
    code_2 : {
        'country' : c_2,
        'region' : r_2,
        'area' : a_2
    },
    code_3 : {
      'country' : c_3,
      'region' : r_3,
      'area' : a_3
    },
})

print(dialing)
dial = input("Please enter the dialing code: ")
print(dialing[dial])