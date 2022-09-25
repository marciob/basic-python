# how to run any python file:
# python fileName.py


print("Mosh Hamedani")
print("0----")
print(" ||||")
print("*" * 10)

price = 10
price = 20
print(price)

is_new = True

name = input("What is your name? ")
color = input("What is your favorite color? ")
print("Hi " + name + ", your favorite is " + color)

birth_year = input("Birth year: ")
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input("What is your weight (in pounds)? ")
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)

course = "Python's Course for Beginners"
print(course)

multipleLines = '''
This is a multiple lines of message,
it's made by adding text within those three quotes.

'''

print(multipleLines)

print(course[0])
print(course[0:3])
print(course[1:5])
print(course[:5])

# formatted strings
variableName = "John"
messageExample = f"Hello {variableName}, good morning!"

# print number of characters
print(len(variableName))

# methods related to string type
variableName.upper()  # it converts the text to uppercase
variableName.find("o")  # it returns the index of the first occurrence of that letter

# //
# division returning just an integer, not a float number
100 // 3

# **
# exponentiation
2 ** 3

# round()
# round numbers
x = 2.9
round(x)

# import math
# it provides complex method calculations
# python 3 version has a different math methods than python 2

is_hot = True
is_cold = False

if is_hot:
    print("")
elif is_cold:
    print("")
else:
    print("")

# and
# or
# not (the opposite of true, equivalent of ! in javascript)


# do an action for each item in an array
for item in ["mosh", "john", "sarah"]:
    print(item)

# nested loops, loop inside a loop
number = [5, 2, 5, 2, 2]
for x_count in number:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

# tuples
# it’s like list but immutable
numbers = (1, 2, 3)

# unpacking
# it’s like javascript destructuring
coordinates = (1, 2, 3)
x, y, z = coordinates
# it’s like:
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]


# dictionaries
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Four"
}

output = ""

for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
    print(output)


# functions
# we use the key world def to define a function
# it's best practice to add two break lines after define a function
# by default all functions return None, to change that and return something it needs to have a return statement
def greet_user(username):
    print(f"Hi {username}!")
    print("Welcome aboard")


greet_user("John")

# try exceptions - handling errors
# it will show a personalized error message when an error occurs, instead of crashing
# in that case the program executes successfully but with an error message before it finishes
# specific kind of errors can be handled, in this example it's handling ValueError type
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")


# classes
# according to name convention first word should be in uppercase
# self is a reference to the current object
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()


#  constructor
# constructors are parameters or logical to run on each new instance of a class
# self is used to define variables inside a constructor

class Movement:
    def __init__(self, moveA, moveB):
        self.moveA = moveA
        self.moveB = moveB

    def move(self):
        print("move")

    def draw(self):
        print("draw")


movement = Movement(10, 20)
movement.moveA = 11
print(movement.moveA)


#  Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  # here Dog is inheriting all methods from Mammal class
    pass  # pass does nothing, it's used just to avoid the IDE complaining for an empty class


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()

