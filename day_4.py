#=============================
# Escape Sequences in Strings
#==============================
'''
print('I hope everyone is enjoying the 30 days python challenge.\nare you?')
print('Days\ttopic\texcersise')
'''
#=============================
# String formatting
#==============================
"""
first_name = 'Parineeta'
last_name = 'Sarkar'
language = 'Python'
print('I am %s %s. I teach %s' %(first_name,last_name,language))

radius = 10
pi = 3.14
area = pi * radius ** 2

print('The area of circle with a radius %d is %.2f' %(radius,area))
"""

#=============================
# New Style String Formatting (str.format)-> (This formatting is introduced in Python version 3.)
#==============================

"""
first_name = 'Parineeta'
last_name = 'Sarkar'
language = 'Python'
print('I am {}. I teach {}'.format(first_name,last_name,language))
a,b=4,3
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} ** {} = {}'.format(a,b,a**b))
"""

#=============================
# New Style String Formatting (str.format)-> (Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject the data in their corresponding positions.)
#==============================

"""
a,b = 4,3
print(f'{a} ** {b} = {a ** b} ')
"""

#=============================
# Python Strings as Sequences of Characters
#==============================

"""
language = 'xyz'
a,b,c = language
print(a)
print(b)
print(c)

language = 'xyz'
print(language[0])
print(language[1])
print(language[2])
"""

#=============================
# Accessing Characters in Strings by Index
#==============================
"""
language = 'Python'
last_index = len(language) - 1
last_string = language[last_index]
print(last_string)
"""
#=============================
# Slicing Python Strings -> (In python we can slice strings into substrings.)
#==============================

"""
language = 'Python'
first_three = language[0:3] # first three letter
last_three = language[3:6] # last three letter

#another way to getting the last three letter
last_three_1 = language[-3:]
# print(last_three_1)

# reverse string

greeting = 'Hello, World'
# print(greeting[::-1]) 

#Skipping Characters While Slicing
pto = language[0:6:2]
print(pto)
"""

#=============================
# String Methods
#==============================

#capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
# print(challenge.capitalize())
#casefold() : Returns a lower case version of the string
# print(challenge.casefold())

#count(): Converts the first character of the string to capital letter
# print(challenge.count('y'))

#=============================
# join(): Returns a concatenated string
#==============================
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
# print(result)
result_1 = "#".join(web_tech)
# print(result_1)
# print(challenge.strip('tha'))
# print(challenge.replace('python','Parineeta'))
# print(challenge.split())
challenge_1 = 'thirty, days, of, python'
# print(challenge_1.split(', '))
# print(challenge.title())
# print(challenge.startswith('thirty'))
print(challenge.startswith('thirtys'))