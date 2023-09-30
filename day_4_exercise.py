"""
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
3. Declare a variable named company and assign it to an initial value "Coding For All".
4. Print the variable company using _print()_.
5. Print the length of the company string using _len()_ method and _print()_.
6. Change all the characters to uppercase letters using _upper()_ method.
7. Change all the characters to lowercase letters using _lower()_ method.
8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
9. Cut(slice) out the first word of _Coding For All_ string.
10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
11. Replace the word coding in the string 'Coding For All' to Python.
12. Change Python for Everyone to Python for All using the replace method or other methods.
13. Split the string 'Coding For All' using space as the separator (split()) .
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
15. What is the character at index 0 in the string _Coding For All_.
16. What is the last index of the string _Coding For All_.
17. What character is at index 10 in "Coding For All" string.
18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
19. Create an acronym or an abbreviation for the name 'Coding For All'.
20. Use index to determine the position of the first occurrence of C in Coding For All.
21. Use index to determine the position of the first occurrence of F in Coding For All.
22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
28. Does '\'Coding For All' start with a substring _Coding_?
29. Does 'Coding For All' end with a substring _coding_?
30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
31. Which one of the following variables return True when we use the method isidentifier():
    - 30DaysOfPython
    - thirty_days_of_python
32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
33. Use the new line escape sequence to separate the following sentences.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
34. Use a tab escape sequence to write the following lines.
    ```py
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
    ```
35. Use the string formatting method to display the following:

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```

36. Make the following using string formatting methods:

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```
"""

# ========================
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# ========================

concate_string = 'Thirty ' + 'Days' + ' Of' + ' Python'
print(concate_string)

# ========================
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
# ========================

s1 = 'Coding'
s2 = 'For'
s3 = 'All'

s = s1 + s2 + s3
print('Concatenated String:', s )

# ========================
# Declare a variable named company and assign it to an initial value "Coding For All".
# ========================

company = "Coding For All"

# ========================
# Print the variable company using print().
# ========================
print("Company:", company)

# ========================
# Print the length of the company string using len() method and print()..
# =======================

print('Compnay length: ', len(company))

# ========================
# Change all the characters to uppercase letters using upper() method.
# =======================

print('Compnay upper case: ', company.upper())

# ========================
# Change all the characters to lowercase letters using lower() method.
# =======================

print('Compnay Lower case: ', company.lower())

# ========================
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# =======================
print('Capitalize: ', company.capitalize())
print('Title: ', company.title())
print('Swapcase: ', company.swapcase())

# ========================
# Cut(slice) out the first word of Coding For All string.
# =======================

slice_string = 'Coding For All'
print(slice_string[1:])

# ========================
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# =======================
index_string = 'Coding For All'
sub_string = 'Coding'
# print(index_string.index(sub_string))
print(index_string.rindex(sub_string))

# ========================
# Replace the word coding in the string 'Coding For All' to Python.
# =======================
replace_str = 'Coding'
print(replace_str.replace('Coding','Coding For All'))

# ========================
# Change Python for Everyone to Python for All using the replace method or other methods.
# =======================
replace_str_1 = 'Python for Everyone'
print(replace_str_1[:11] + 'All')
print(replace_str_1.replace('Everyone','All'))

# ========================
# Split the string 'Coding For All' using space as the separator (split()) .
# =======================

split_str = 'Coding For All'
print("split string: ", split_str.split(' '))

# ========================
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# =======================

split_str_1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("Split String: ", split_str_1.split(','))

# ========================
# What is the character at index 0 in the string Coding For All.
# =======================

find_chr = 'Coding For All'
print("'{}' : {}".format(find_chr,find_chr[:1]))
print("'{}' : {}".format(find_chr,find_chr[0]))

# ========================
# What is the last index of the string Coding For All.
# =======================
find_chr_1 = 'Coding For All'
last_ind = len(find_chr_1) - 2
print("'{}' : {}".format(find_chr_1[-1:],last_ind))

# ========================
# What character is at index 10 in "Coding For All" string.
# =======================
find_chr_2 = 'Coding For All'
print("'{}' : {}".format(find_chr_2,find_chr_2[-1]))

# ========================
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# =======================
abbrv_name = 'Python For Everyone'
print("{}".format((abbrv_name[:-3])))

# ========================
# Create an acronym or an abbreviation for the name 'Coding For All'.
# =======================
abbrv_name_1 = 'Coding For All'
print('{} {}'.format(abbrv_name_1,abbrv_name_1[:3]))

# ========================
# Use index to determine the position of the first occurrence of C in Coding For All.
# =======================
index_of_c = 'Coding For All'
print("'C' Index In '{}' Is At Position {} ".format(index_of_c,index_of_c.lower().find('c')))

# ========================
# Use index to determine the position of the first occurrence of F in Coding For All.
# =======================
index_of_f = 'Coding For All'
print("'F' Index In '{}' Is At Position {}".format(index_of_f,index_of_f.lower().find('f')))

# ========================
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
# =======================

rfind_l = ' Coding For All People'
print('Last occurrence of L: ',rfind_l.rfind('l'))

# ========================
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# =======================
index_of_because = 'You cannot end a sentence with because because because is a conjunction'
print("Occurrence of 'because': ", index_of_because.find("because"))

# ========================
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# =======================
index_of_because_1 = 'You cannot end a sentence with because because because is a conjunction'
print("Last Occurrence of 'because': ", index_of_because.rindex("because"))

# ========================
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# =======================

sentence  = "You can't end a sentence with because because because is a conjunction"
# Find the index of the first occurrence of 'because'
first_occurrence = sentence.find('because')
# Find the index of the last occurrence of 'because' using a loop
last_occurrence = sentence.rindex('because')
print(sentence[first_occurrence:last_occurrence])
print(sentence[:first_occurrence] + sentence[last_occurrence + len('because'):])

# ========================
# Does 'Coding For All' start with a substring Coding?
# =======================

if 'Coding For All'.startswith('Coding') == True:
    print ("Yes")
else:
    print ('No')

# ========================
# Does 'Coding For All' end with a substring coding?
# =======================

if 'Coding For All'.endswith('Coding') == True:
    print ("Yes")
else:
    print ('No')

# ========================
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# strip(): method removes both leading and trailing spaces (and other whitespace characters like tabs and newline characters) from the given string, leaving you with the desired result.
# =======================
s= '    Coding for all     '
print(s.strip())

# ========================
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
# =======================
a='30DaysOfPython'
b ='thirty_days_of_python'
if a.isidentifier() == True:
    print ('Yes')
else:
    print('No')

if b.isidentifier() == True:
    print('Yes')
else:
    print('No')

# ========================
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# ========================
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# ========================
# Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
# I just wonder what is next.
# ========================
print('I am enjoying this challenge. \nI just wonder what is next.')

# ========================
# Use the new line escape sequence to separate the following sentences.
# Name      Age     Country   City.
# Asabeneh  250     Finland   Helsinki
# ========================
print('Name \t Age \t Country \t City')
print('Asabeneh \t 250 \t Finland \t Helsinki')
data = """ Name      Age     Country   City.
Asabeneh  250     Finland   Helsinki
"""
print(data)

# ========================
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# ========================
radius = 10
area = 3.14 * radius ** 2
print('{} * {} ** 2 = {}'.format(3.14,radius,area))

# ========================
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
# =======================
x,y = 8,6
print('{} + {} = {}'.format(x,y,x + y))
print('{} - {} = {}'.format(x,y,x - y))
print('{} * {} = {}'.format(x,y,x * y))
print('{} / {} = {}'.format(x,y,x / y))
print('{} // {} = {}'.format(x,y,x // y))
print('{} ** {} = {}'.format(x,y,x ** y))
print('{} % {} = {}'.format(x,y,x % y))
print()
print('======================================')
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} * {y} = {x * y}')
print(f'{x} / {y} = {x / y}')