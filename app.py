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
variableName.upper() # it converts the text to uppercase
variableName.find("o") # it returns the index of the first occurrence of that letter
