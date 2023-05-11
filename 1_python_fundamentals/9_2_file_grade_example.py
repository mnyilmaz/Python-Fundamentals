# BTK Academy
# Advanced Python Programming From Zero
# Lecture 9.2: File Extension in Python - Grade Example
# python 9_2_file_grade_example.py
blank = "----------------------"

def lg(gr):
    if gr > 90:
        print(f"Overall grade: {gr}\nLetter grade: AA")
    elif 85 < gr < 89:
        print(f"Overall grade: {gr}\nLetter grade: BA")
    elif 80 < gr < 84:
        print(f"Overall grade: {gr}\nLetter grade: BB")
    elif 75 < gr < 79:
        print(f"Overall grade: {gr}\nLetter grade: CB")
    elif 70 < gr < 74:
        print(f"Overall grade: {gr}\nLetter grade: CC")
    elif 65 < gr < 69:
        print(f"Overall grade: {gr}\nLetter grade: DC")
    elif 60 < gr < 64:
        print(f"Overall grade: {gr}\nLetter grade: DD")
    elif 50 < gr < 59:
        print(f"Overall grade: {gr}\nLetter grade: FD")
    elif gr < 49:
        print(f"Overall grade: {gr}\nLetter grade: FF")


def grade_calc():
    with open("overall.txt", "r", encoding="utf-8") as ovrll:
        list = ovrll.readlines()
        list = list[0].split(":")
        ovrall = float(list[1])
        print(f"{list[0]}'s\n{lg(ovrall)}")
            
def reveal_grades():
    with open("grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)
        print(grade_calc())

def enter_grades():
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    grade_1 = int(input("Please enter your first grade: "))
    grade_2 = int(input("Please enter your second grade: "))
    grade_3 = int(input("Please enter your third grade: "))

    with open("overall.txt", "a") as overall:
        grd = ((grade_1 + grade_2)*0.60) + ((grade_3)*0.40)
        overall.write(f"\n{name} {surname} : {grd}\n")

    with open("grades.txt", "a", encoding="utf-8") as grds:
        # grds.write(name + "" + surname + "" + ":" + "\n" + "Grade 1:" + "" + grade_1 + "\n" + "Grade 2:" + "" + grade_2 + "\n" + "Grade 3:" + "" + grade_3)
        grds.write(f"{name} {surname}\nFirst Grade: {grade_1}\nSecond Grade: {grade_2}\nThird Grade: {grade_3}\n{blank}\n")


while True:
    process = input("1 - Reveal Grades (Press: R)\n2 - Enter Grades(Press: E)\n3 - Exit(Press: Q)\n")
    if process == "R":
        reveal_grades()
    elif process == "E":
        enter_grades()
    elif process == "Q":
        break

