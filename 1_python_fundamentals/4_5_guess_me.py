# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.5: Loops in Pyhton - Loop Examples - Number Guessing Game
# python 4_5_guess_me.py
blank = "----------------------"
import random

# Number Guessing Game

"""
RULES:
# 1 : Number must be between 1 - 100.
# 2 : Random module will be used during system.
# 3 : Every question for guessing the number has point and it is related to amount of right (for 5 rights 20 points).
# 4 : User will determine the rights for accurate guess.
# 5 : Every question will be calculated over amount of rights.
"""

guess_me = random.randint(1,100)
# guess_me = int(random.random()*100)

right = int(input("Please enter your entitlement amount: "))
total_point = 100

while right > 0:
    right_point = total_point / right
    right -= 1
    remaining_point = total_point - right_point
    guess = int(input("Guess me: "))

    if guess != guess_me and guess > guess_me and right >= 1:
        total_point -= right_point
        print(total_point)
        print(f"{right} left. Decrease your guess and try again.")

    elif guess != guess_me and guess < guess_me and right >= 1:
        total_point -= right_point
        print(total_point)
        print(f"{right} left. Increase your guess and try again.")
  
    elif guess == guess_me:
        print(f"Congratulations! You've guessed {guess_me} and won {remaining_point} points.")
        try_again = input("Do you want to try again (Y/N)?: ")
        if try_again == "Y":
            guess_me = random.randint(1,100)
            total_point = 100
            right = int(input("Please enter your entitlement amount: "))
        if try_again == "N":
            print("Thanks for playing!")

    else:
        print(f"You've run out of rights. Correct number was {guess_me} and your total point is {remaining_point}.")
        try_again = input("Do you want to try again (Y/N)?: ")
        if try_again == "Y":
            guess_me = random.randint(1,100)
            total_point = 100
            right = int(input("Please enter your entitlement amount: "))
        if try_again == "N":
            print("Thanks for playing!")
            break
        

