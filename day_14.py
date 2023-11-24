from functools import reduce


def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

result  = add_ten()
print(result(5))

def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper
@split_string_decorator
@uppercase_decorator
def greeting_1():
    return 'Welcome to Python1'
print(greeting_1())

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(param1,param2,param3):
        function(param1,param2,param3)
        print("I live in {}".format(param3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name,last_name,country):
    print("I am {} {}. I love to teach.".format(first_name,last_name,country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

# The map() function is a built-in function that takes a function and iterable as parameters.
numbers = [1,2,3,4]
def square(x):
    return x ** 2
numbers_squared = map(square,numbers)
print(list(numbers_squared))

def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even,numbers)
print(list(even_numbers))

# Python - Reduce Function


# ===========================================================Exercises===========================================#
countries_1 = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names_1 = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ========================
# Explain the difference between map, filter, and reduce.
# ========================
print("The map function is bult in function that takes a function and iterable as parameter")
def cube(num):
    return num ** 3

res = list(map(cube,numbers_1))
# print(res)

print("The filter function calls the specified function which return boolean for each item of the specified iterable (list)")

def not_even(num):
    if num % 2 != 0:
        return num
res_1 = list(filter(not_even,numbers_1))
# print(res_1)

print("Like map and filter function it takes two parameters, a function and iterable, instead it returns a single value,It does not return another iterable")

def add_two_numbers(x,y):
    return int(x) + int(y)

total = reduce(add_two_numbers,numbers_1)
print(total)

# ========================
# Explain the difference between higher order function, closure and decorator
# ========================
higher_order_function = """
In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable
"""

print(higher_order_function)

closure = """
Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.
"""

def add_nine():
    nine = 9
    def add(num):
        return num+nine
    return add
closure_result_1 = add_nine()
print(closure_result_1(5))

decorator = """
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
"""

'''This decorator function is a higher order function
that takes a function as a parameter'''

def uppercase_decorator_1(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator_1
def greeting_1():
    return "Welcome to my world"
print(greeting_1())

# ========================
# Use for loop to print each country in the countries list.
# ========================

for country in countries_1:
    print(country,end='\n')
print()
# ========================
# Use for to print each name in the names list.
# ========================

for name in names_1:
    print(name,end='\n')
print()
# ========================
# Use for to print each number in the numbers list.
# ========================

for number in numbers_1:
    print(number,end='\n')
print()

# ========================
# Use map to create a new list by changing each country to uppercase in the countries list
# ========================

def uppercase_countries(countries):
    return countries.upper()

res_2 = map(uppercase_countries,countries_1)
print(list(res_2),end='\n')

# ========================
# Use map to create a new list by changing each number to its square in the numbers list
# ========================

def squere_list(num):
    return num**2
res_3 = map(squere_list,numbers_1)
print(list(res_3),end='\n')

# ========================
# Use map to change each name to uppercase in the names list
# ========================

def uppercase_names(names):
    return names.upper()
res_4 = list(map(uppercase_names,names_1))
print(res_4,end='\n')

# ========================
# Use filter to filter out countries containing 'land'.
# ========================

def filter_out_land(countries):
    if countries.find('land') != -1:
        return countries
filter_out_countries = filter(filter_out_land,countries_1)
print(list(filter_out_countries),end='\n')

# ========================
# Use filter to filter out countries having exactly six characters
# ========================

def count_words(countries):
    if len(countries) == 6:
        return countries
res_5 = filter(count_words,countries_1)
print(list(res_5),end='\n')

# ========================
# Use filter to filter out countries having exactly six characters
# ========================
filtered_countries = list(filter(lambda coutry: len(country) >=6,countries_1))
print(filtered_countries)

# ========================
# Use filter to filter out countries starting with an 'E'
# ========================
start_with_E = list(filter(lambda country: country.startswith('E'),countries_1))
print(start_with_E)

# ========================
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# ========================


squared_numbers = map(lambda square: square **2,numbers_1)
even_numbers = filter(lambda even: even % 2 == 0,squared_numbers)
chain_list = reduce(lambda x,y: int(x) + int(y),even_numbers)
print(chain_list)

# ========================
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# ========================
mixed_lst = [1,'sdfs','sdfsf',3,'erter']
is_string = list(filter(lambda is_string: type(is_string) == str,mixed_lst))
print(is_string)

# ========================
# Use reduce to sum all the numbers in the numbers list.
# ========================
total_sum = reduce(lambda x,y: x + y, numbers_1)
print(total_sum)

# ========================
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# ========================
concatenate_country_lst =  reduce(lambda a,b: a + ',' + b,countries_1)
print(concatenate_country_lst)

lst = ""
for index,item in enumerate(countries_1):
    if index == len(countries_1) - 1:
        lst += '' + item
    else:
        lst += item + ','
print(lst)

# ========================
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# ========================
from countries import *
# print(Countries)
def count_countries_by_starting_letter(coutrylist):
    letter_count = {}
    for coutry in coutrylist:
        first_letter = coutry[0].upper()
        if first_letter not in letter_count:
            letter_count[first_letter] = 1
        else:
            letter_count[first_letter] += 1
    return letter_count

print(count_countries_by_starting_letter(Countries))

# ========================
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# ========================
def get_first_ten_countries(coutrylist):
    first_ten = []
    for i in range(10):
        first_ten.append(coutrylist[i])
    return first_ten

print(get_first_ten_countries(Countries))

def get_first_ten_countries_1(coutrylist):
    return coutrylist[:10]
print(get_first_ten_countries_1(Countries))

# ========================
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
# ========================


def get_last_ten_countries(coutrylist):
    first_ten = []
    cn_len = len(coutrylist)
    for i in range(cn_len-10,cn_len):
        first_ten.append(coutrylist[i])
    return first_ten

print(get_last_ten_countries(Countries))

def get_last_ten_countries_1(coutrylist):
    return coutrylist[-10:]
print(get_last_ten_countries_1(Countries))