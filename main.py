"""
-----Q1-----

# TODO: Create an integer variable named 'age' with your age
age = 26
# TODO: Create a float variable named 'height' with your height in meters
height = 1.70
# TODO: Create a string variable named 'name' with your name
name = "Mehdi Zitouni"
# TODO: Create a boolean variable named 'is_student' and set it to True
is_student = True
# Print all variables and their types
# Example: print(f"Age: {age}, Type: {type(age)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Taille: {height}, Type: {type(height)}")
print(f"Nom: {name}, Type: {type(name)}")
print(f"est étudiant: {is_student}, Type: {type(is_student)}")
"""

"""
-----Q2-----

# TODO: Create two variables 'a' and 'b' with numeric values
a = 6
b = 2
# TODO: Perform addition, subtraction, multiplication, and division of a and b
# Print the results of each operation

add = print(a+b)
sub = print(a-b)
mult = print(a*b)
div = print(a/b)

# TODO: Calculate the remainder of a divided by b using the modulo operator

remainder = print(f"Remainder : {a % b}")

# TODO: Calculate a to the power of b using the exponentiation operator

power = print(f"Power : {a ** b}")
"""

"""
-----Q3-----
# TODO: Create two string variables 'first_name' and 'last_name'
first_name = 'Mehdi'
last_name = 'Zitouni'
# TODO: Concatenate the two names to create a 'full_name' variable
full_name = first_name + " " + last_name
# TODO: Print the full name in uppercase
print(full_name, full_name.upper())
# TODO: Print the length of the full name
print(full_name, len(full_name))
# TODO: Create a string with multiple words and split it into a list
phrase = "Je m'appelle Mehdi"
print(phrase, phrase.split())
"""

"""
-----Q4-----
# TODO: Convert a string containing a number to an integer
name = "Me3hdi22"
print(f"nom : {name}, {type(name)}")
number_extract = ''.join(i for i in name if i.isdigit())
name_convert = int(number_extract)
print(f"nom : {name_convert}, {type(name_convert)}")

# TODO: Convert a float to an integer
decimal = 1.70
entier = int(decimal)
print(f"Nouvel entier : {entier}, type : {type(entier)}")
# TODO: Convert an integer to a float
entier2 = 2
decimal2 = float(entier2)
print(f"Nouveau décimal : {decimal2}, type : {type(decimal2)}")

# TODO: Convert a number (integer or float) to a string
nombre = 25.3
nouveau_mot = str(nombre)
print(f"Nouveau mot : {nouveau_mot}, type : {type(nouveau_mot)}")
# Print all converted values and their new types
"""

# -----Q5-----
# TODO: Create two boolean variables
is_bg = True
is_tall = False
print(is_bg)
print(is_tall)

# TODO: Perform AND, OR, and NOT operations on these variables
is_grand_bg = is_bg and is_tall
print(f"est grand ET bg : {is_grand_bg}")

is_grand_ou_bg = is_bg or is_tall
print(f"est grand OU bg : {is_grand_ou_bg}")

not_is_bg = not is_bg
print(f"est moche : {not_is_bg}")

# Print the results

# TODO: Create two numeric variables and use comparison operators
# (>, <, >=, <=, ==, !=) to compare them
x = 52
y = 34.2

result_1 = x > y
result_2 = x < y
result_3 = x >= y
result_4 = x <= y
result_5 = x == y
result_6 = x != y
# Print the results of these comparisons
print(f"x supérieur à y : {result_1}")
print(f"x inférieur à y : {result_2}")
print(f"x supérieur ou égal à y : {result_3}")
print(f"x inférieur ou égal à y : {result_4}")
print(f"x est égal à y : {result_5}")
print(f"x est différent de y : {result_6}")
