# BTK Academy
# Advanced Python Programming From Zero
# Lecture 6.2: Object Oriented Programming in Python - Inheritance
# python 6_2_oop_inheritance.py
blank = "----------------------"

# Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from 
# another class. Parent class is the class being inherited from, also called base class. 
# Child class is the class that inherits from another class, also called derived class.

class Driver():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print("Driver added")

    def who_am_i(self):
        print("F1 driver")

    def rise(self):
        print("Let's keep pushing")

class Leclerc(Driver):
    def __init__(self, name, surname, team_points):
        # or super().__init__(name, surname)
        Driver.__init__(self, name, surname) # to keep info from upper class
        self.team_points = team_points
        print("Team updated")
    
    # override
    def who_am_i(self):
        print("F1 driver")
    
    def podiums(self):
        return 18

sainz = Driver("Carlos", "Sainz")
leclerc = Leclerc("Charles", "Leclerc", 233)
print(blank)
sainz.who_am_i() 
sainz.rise()
print(blank)
leclerc.who_am_i()
leclerc.rise()
print(blank)

print(f"Driver's name: {sainz.name}\nDriver's surname: {sainz.surname}")
print(blank)
print(f"Driver's name: {leclerc.name }\nDriver's surname: {leclerc.surname}\nDriver's point: {str(leclerc.team_points)}\nPodiums: {leclerc.podiums()}")
print(blank)

##############################################################################################################

# Special Methods

class Movie():
    def __init__(self, title, director, composer, duration):
        self.title = title
        self.director = director
        self.composer = composer
        self.duration = duration
        print("Movie has selected")

    def __str__(self):
        return f"Title: {m.title}\nDirector: {m.director}\nComposer: {m.composer}\nDuration: {m.duration} min."
    
    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie has deleted")

m = Movie("Inception", "Christopher Nolan", "Hans Zimmer", 148)
print(str(m))
print(f"{len(m)} minutes")
del m

# print(f"Title: {m.title}\nDirector: {m.director}\nComposer: {m.composer}")


