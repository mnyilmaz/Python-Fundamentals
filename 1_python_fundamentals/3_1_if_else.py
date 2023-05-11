# BTK Academy
# Advanced Python Programming From Zero
# Lecture 3.1: Conditional Statements in Pyhton - If Else
# python 3_1_if_else.py
blank = "----------------------"
from datetime import date
import datetime

# If - Else
username = input("Username:" )
password = input("Password:" )

is_logged = (username == "alice") and (password == "wonderland")

if (username == "alice"):
    if (password == "wonderland"):
        print("Login Successfull!")
    else:
        print("Incorrect Password!")
else: 
    print("User could not be authenticated!")

print(blank)

##############################################################################################################

# Elif
x = int(input("x = "))
y = int(input("y = "))

if x > y:
    print(f"{x} is greater than {y}")

elif x == y:
    print(f"{x} is equal to {y}")

else:
    print(f"{y} is greater than {x}")

print(blank)

##############################################################################################################

# Example 1 : Working with if - else - elif

# 1 - Get name, age and educational status from user to check availability for getting driver license.
# Candidate drive must be at least 18 and educational status must be high school or higher.

d_name = input("Please enter your name: ")
d_age = int(input("Please enter your age: "))
d_edu = input("Please enter your educational status: ")

print(f"Welcome to the registration {d_name}")
if d_age >= 18:
    if (d_edu == "High School") or (d_edu =="University"):
         print(f"{d_name}'s age is {d_age} and educational status is {d_edu}. Proper for driver license.")
    else: 
        print(f"{d_name}'s educational status is {d_edu}. Not proper for driver license.")
else: 
    print(f"{d_name}'s age is {d_age}. Not proper for driver license.")

print(blank)

##############################################################################################################

# 2 - Get two exam and one pratice exam results from the user. 
# Percentanes will be %60 for exam and %40 for pratice exam. 

ex_1 = int(input("Please enter the first midterm exam result: "))
ex_2 = int(input("Please enter the second midterm exam result: "))
practice = int(input("Please enter the final exam result: "))
average = (((ex_1 + ex_2)//2)*0.6) + (practice*0.4)

if 0 <= average <= 24:
    print(f"Average is {average} and grade is 0")
elif 25 <= average <= 44:
   print(f"Average is {average} and grade is 1")
elif 45 <= average <= 54:
   print(f"Average is {average} and grade is 2")
elif 55 <= average <= 69:
   print(f"Average is {average} and grade is 3")
elif 70 <= average <= 84:
   print(f"Average is {average} and grade is 4")
elif average >= 85:
     print(f"Average is {average} and grade is 5")

print(blank)

##############################################################################################################

# 3 - Calculate the service time of a vehicle whose registration date is taken.
# Time calculation must be made by using day based.
# Use datetime module.

vehicle_date = input("Please enter your vehicle's registration date (YY/MM/DD): ")
vehicle_date = vehicle_date.split("/")

# vehicle_date[0] = int(vehicle_date[0])
# vehicle_date[1] = int(vehicle_date[1])
# vehicle_date[2] = int(vehicle_date[2])

# today_date = date.today()
# service_year = today_date.year - vehicle_date[0]
# print("Year:", service_year)
# service_month = today_date.month - vehicle_date[1]
# print("Month:",service_month)
# service_day = (service_year*365) + (service_month*30) + vehicle_date[2]
# print("Day:",service_day)

reg_date = datetime.datetime(int(vehicle_date[0]), int(vehicle_date[1]), int(vehicle_date[2]))
today_date = datetime.datetime.now()
service_day = today_date - reg_date


if service_day.days < 365:
    print(f"Service day is {service_day.days}. Car is not old enough for maintanance")
elif service_day.days == 365:
    print(f"Service day is {service_day.days}.First car maintanance.")
elif 730 <= service_day.days < 1095:
    print(f"Service day is {service_day.days}.Second car maintanance.")
elif service_day.days == 1095:
    print(f"Service day is {service_day.days}.Third car maintanance.")
else:
    print(f"Service day is {service_day.days}.Car is old enough for further maintanance.")


