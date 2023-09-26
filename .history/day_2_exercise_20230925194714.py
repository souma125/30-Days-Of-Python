"""
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line
"""

"""
1. Check the data type of all your variables using type() built-in function
1. Using the _len()_ built-in function, find the length of your first name
1. Compare the length of your first name and your last name
1. Declare 5 as num_one and 4 as num_two
    1. Add num_one and num_two and assign the value to a variable total
    2. Subtract num_two from num_one and assign the value to a variable diff
    3. Multiply num_two and num_one and assign the value to a variable product
    4. Divide num_one by num_two and assign the value to a variable division
    5. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    6. Calculate num_one to the power of num_two and assign the value to a variable exp
    7. Find floor division of num_one by num_two and assign the value to a variable floor_division
1. The radius of a circle is 30 meters.
    1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
    2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
    3. Take radius as user input and calculate the area.
1. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
1. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

# ========================
# Day 2: 30 Days of python programming
# ========================
first_name = 'Parineeta'
last_name = 'Sarkar'
full_name = first_name + ' ' + last_name
country = 'India'
city = 'Kolkata'
monthe_str = ' months'
age = str(17) + monthe_str
year = 2022
is_married = False
is_true = True
is_light_on = False
a= b= c = 10
print("Full Name:", full_name,"\nCountry:", country,"City", city ,"Age : ", age )
print(type(first_name)) # <class 'str'>
print(type(last_name)) # <class 'str'>
print(type(full_name)) # <class 'str'>

print(type(country)) # <class 'str'>
print(type(city)) # <class 'str'>

print(type(age)) # <class 'int'>
print(type(is_married)) # <class 'bool'>
print(type(is_light_on)) # <class 'bool'>

print(type(a)) # <class 'int'>
print(type(b)) # <class 'int'>
print(type(c)) # <class 'int'>

first_name_len = len(first_name)
last_name_len = len(last_name)

if first_name_len > last_name_len:
    print('first name is bigger than last name')
else:
    print('last name is bigger than first name')

num_one,num_two = 5,4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_two / num_one
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_two // num_one

print("total:", total)
print("diff:", diff)
print("product:", product)
print("division:", division)
print("remainder:", remainder)
print("exp:", exp)
print("floor_division:", floor_division)

# ========================
# 1. Take radius as user input and calculate the area.
# ========================
import math
radius = float (input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius ** 2
print("The area of the circle is: ", area_of_circle)

# ========================
# 2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
# ========================

radius_1 = float (input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius ** 2
print("The area of the circle is: ", area_of_circle)

