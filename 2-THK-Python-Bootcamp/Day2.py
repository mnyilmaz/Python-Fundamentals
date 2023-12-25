# THK_Python_Bootcamp_Day_2
# NOTES

# Make a guess game, PC will hold the number, use random library
import random

# list = ["a","b","c","d","mny",7,9,1]
# print(random.choice(list))

number = random.randint(1, 10)
i=1
while i<=7:
    userNum = int(input("Enter your guess = "))
    if 0 < userNum < 11:
         if number == userNum:
            print("Your guess is correct on your ", i, ". right")
            print("Guessed number is = ", userNum)
            print("Actual number is = ", number)
            break

         elif number > userNum:
            print("Increase your guess.")
         elif number < userNum:
            print("Decrease your guess.")

    else:
        print("Your value is out of boundaries")
    i += 1

if number != userNum:
    print("Your game is over. Actual number is = ", number)

# For Loop

for x in range(1, 101, 2):
    # will begin from 1, go until 100 and increase by twos
    print(x)

games = ["Death Stranding", "RDR 2", "Uncharted", "Tomb Raider"]
for y in games:
    print(y)

