# ========================
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# ========================
def add_two_numbers(a, b):
    result = 0
    result = a + b
    return result
print(add_two_numbers(4,5))

# ========================
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# ========================
import math
def area_of_circle(r):
    return math.pi * r * r

print(area_of_circle(5))

# ========================
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# ========================
def add_all_nums(*nums):
    total_sum = 0
    for num in nums:
       if isinstance(num,(int,float)):
           total_sum += num
       else:
           return "Please enter only numbers"
    return total_sum
    
print(add_all_nums(2, 3, 5))

# ========================
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# ========================

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print("Celsius to Fahrenheit",convert_celsius_to_fahrenheit(10),'\n')

# ========================
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# ========================

def check_season(month):
    if month == 'January' or month=='March':
        return 'Winter'
    elif month == 'April' or month == 'Octobor':
        return 'Summer'
    elif month == 'November' or month == 'December':
        return 'Winter'
    else:
        return ('Invalid Month!')
print(check_season('November'))

# ========================
# Write a function called calculate_slope which return the slope of a linear equation
# ========================
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("The x-coordinates must be different to calculate the slope.")
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Example usage:
x1, y1 = 2, 3
x2, y2 = 5, 9
slope = calculate_slope(x1, y1, x2, y2)
print("The slope of the line is:", slope)

# ========================
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# ========================

import math

def solve_quadratic_eqn(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is positive, zero, or negative to determine the number of solutions
    if discriminant > 0:
        # Two real and distinct solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        # One real solution (double root)
        root1 = -b / (2*a)
        return root1
    else:
        # Complex solutions (no real roots)
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2)

# Example usage:
a = 1
b = -3
c = 2
solutions = solve_quadratic_eqn(a, b, c)
print("Solutions:", solutions)

# ========================
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# ========================

def print_list(lst):
    for item in lst:
        print(item,'\n')

print(print_list([1,2,3]))

# ========================
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# ========================
def reverse_list(lst_1):
    lst_2=[]
    for i in range(len(lst_1) -1,-1,-1):
        lst_2.append(lst_1[i])
    return lst_2
print(reverse_list([1,2,3]))

# ========================
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# ========================
def capitalize_list_items(lst_3):
    lst_4 = []
    for word in lst_3:
        # word=word.capitalize()
        # word=word[:].capitalize()
        # lst_4.append(word)
        lst_4.append(word.capitalize())
    return lst_4
print(capitalize_list_items(['hello','world']))

# ========================
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# ========================

def add_item(lst,item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat')) 

# ========================
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# ========================
def remove_item(lst,item):
    lst.remove(item)
    return lst
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3)) 

# ========================
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# ========================
def sum_of_numbers(num):
    total = 0
    for i in range(0,6):
        total += i
    return total
print("Sum of numbers from zero to five is",sum_of_numbers(5));

# ========================
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# ========================

def sum_of_odds(lst):
    total_sum = 0
    for num in lst :
        if num % 2 != 0:
            total_sum+=num
    return total_sum
print('The Sum Of Odd Numbers In List Is:',sum_of_odds([1 ,8 ,-2,-1]))

# ========================
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# ========================
def sum_of_even(lst):
    total_sum = 0
    for num in lst :
        if num % 2 == 0:
            total_sum+=num
    return total_sum
print('The Sum Of even Numbers In List Is:',sum_of_even([1 ,8 ,-2,-1]))

# ========================
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# ========================
def evens_and_odds(nums):
    even_count = 0
    odd_count = 0
    for i in range(nums):
        if i % 2 == 0:
            even_count += 1
        if i % 2 != 0:
            odd_count += 1
    return (odd_count,even_count)
print(evens_and_odds(100))

# ========================
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# ========================
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# ========================
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# ========================
def is_empty(n):
    if len(n) <= 0:
        return -1
    else:
        return 1
n = ""
if is_empty(n) == -1:
    print("empty")
else:
    print("not Empty")

# ========================
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# ========================

def calculate_mean(data):
    if len(data) == 0:
        return None
    total = sum(data)
    mean = total / len(data)
    return mean
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]
    return median
from collections import Counter

def calculate_mode(data):
    count = Counter(data)
    mode = [key for key, value in count.items() if value == max(count.values())]
    return mode
def calculate_range(data):
    if len(data) == 0:
        return None
    data_range = max(data) - min(data)
    return data_range
def calculate_variance(data):
    if len(data) == 0:
        return None
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance
import math

def calculate_std(data):
    variance = calculate_variance(data)
    if variance is None:
        return None
    std_deviation = math.sqrt(variance)
    return std_deviation
data = [2, 4, 4, 4, 5, 5, 7, 9]
mean = calculate_mean(data)
median = calculate_median(data)
mode = calculate_mode(data)
data_range = calculate_range(data)
variance = calculate_variance(data)
std_deviation = calculate_std(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

# ========================
# Write a function called is_prime, which checks if a number is prime.
# ========================
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True
print(is_prime(2))  # True
print(is_prime(17)) # True
print(is_prime(10)) # False
print(is_prime(1))  # False

# ========================
# Write a function which check if provided variable is a valid python variable
# ========================
import keyword

def is_valid_variable_name(variable_name):
    if not variable_name.isidentifier():
        return False  # Not a valid identifier
    
    if keyword.iskeyword(variable_name):
        return False  # It's a Python keyword
    
    return True

# Examples
print(is_valid_variable_name("valid_var"))  # True
print(is_valid_variable_name("123invalid"))  # False (starts with a digit)
print(is_valid_variable_name("for"))         # False (Python keyword)
print(is_valid_variable_name("in"))          # False (Python keyword)

