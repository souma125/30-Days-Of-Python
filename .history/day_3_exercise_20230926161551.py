"""
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
 4.1 Enter base: 20
    Enter height: 10
    The area of the triangle is 100
5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and between point (2, 2) and point (6,10) 
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text _python_ and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
 21.1
    Enter hours: 40
    Enter rate per hour: 28
    Your weekly earning is 1120
22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
  22.1
  Enter number of years you have lived: 100
  You have lived for 3153600000 seconds.
"""
# ========================
# 1. Declare your age as integer variable
# 2. Declare your height as a float variable
# 3. Declare a variable that store a complex number
# ========================
age = 31
height = 31.1
complex_num = 1 + 2j

# ========================
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# ========================
base = int(input('Enter the base of an area: '))
height = int(input('Enter the height of an area: '))
area = 0.5 * base * height
print("Total area is ", area)

# ========================
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter =  of the triangle (perimeter = a + b + c).
# ========================
side_a = int(input('Enter the side a of an area: '))
side_b = int(input('Enter the side b of an area: '))
side_c = int(input('Enter the side c of an area: '))
perimeter = side_a * side_b * side_c
print("Perimeter is ", perimeter)

# ========================
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# ========================
length = float(input('Enter the lenght of an area: '))
width = float(input('Enter the widtht of an area: '))
area = length * width
perimeter = 2 * (length + width)

print("The area of the rectangle is", area, "square units.")
print("The perimeter of the rectangle is", perimeter, "units.")

# ========================
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
# ========================
import math
circle_radius = float(input('Enter the radius of an circle: '))
circle_area = math.pi * circle_radius * circle_radius
circle_circumference = 2 * math.pi * circle_radius

print("The area of the circle is", circle_area, "square units.")
print("The circumference of the circle is", circle_circumference, "units.")

# ========================
# 8.Calculate the slope, x-intercept and y-intercept of y = 2x -2
# ========================
import numpy as np

# Define the function
def y(x): # doubles a number and then subtracts 2
 return 2*x - 2

# Create a numpy array of x values
x = np.linspace(-10, 10, 100)

# Calculate the y values
y_values = y(x)

# Calculate the slope using linear regression
slope, intercept = np.polyfit(x, y_values, 1)

# Print the slope and intercept
print("Slope:", slope)
print("Intercept:", intercept)

# ========================
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# ========================

# ========================
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# ========================

first_len = len('python')
sec_len = len('dragon')
if first_len != sec_len:
    print(False)
else:
   print(True)

# ========================
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# ========================
if 'on' in 'python' and 'on' in 'dragon':
   print('on is found in both python and dragon')
else:
   print('on is not found in both python and dragon')

# ========================
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# ========================