language = 'Parineeta'
lst = [i for i in language]
print(lst)

# Generating numbers
numbers = [i for i in range(11)]
print(numbers)

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)
# It is also possible to make a list of tuples
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
numbers_1 = [(i, i * i) for i in range(11)]
print(numbers_1)

# List comprehension can be combined with if expression
even_num = [i for i in range(11) if i % 2 == 0 ]
print(even_num)

odd_numbers = [i for i in range(11) if i % 2 != 0]
print(odd_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for row in list_of_lists for item in row]
print(flattened_list)

# Creating a Lambda Function
addd_two_nums = lambda a,b: a + b
result = addd_two_nums(3, 5)
print(result)
# Self invoking lambda function
print((lambda a, b: a + b)(2,3)) # 5 - need to encapsulate it in print() to see the result in the console
square = lambda a: a ** 2
print(square(5))

# Multiple variables
multiple_variable = lambda a,b,c: a ** 2 - b + 1 + 4 * c
print(multiple_variable(2, 3, 4))

# Lambda Function Inside Another Function
def power(a):
    return lambda a: a ** 2
double_power = power(2)
print(double_power(3))

# ================================================Excercises======================================================#

"""
Filter only negative and zero in the list using list comprehension
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero = [i for i in numbers if i <= 0]
print(negative_zero)

"""
Flatten the following list of lists of lists to a one dimensional list :
"""
list_of_lists_1 =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [item for i in list_of_lists_1 for row in i for item in row]
print(flat_list)

"""
Flatten the following list to a new list:
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [country for sublist in countries for country in sublist]
print(flattened_list)
flattened_list_1 = [[country[0].upper(),country[0][:3].upper(),country[1].upper() ] for sublist in countries for country in sublist]
print(flattened_list_1)

"""
Change the following list to a list of dictionaries:
"""

countries_1 = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list_2 = [{'country': country, 'city': city} for country,city in [ item[0] for item in countries]]
print(flattened_list_2)

"""
Change the following list of lists to a list of concatenated strings:
"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flattened_list_3 = [a+' '+b for a,b in [item[0] for item in names]]
# concatenated_string = " ".join([str(name) for name in flattened_list_3])
print(flattened_list_3)
