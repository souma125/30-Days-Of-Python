"""
### Exercises: Level 1

1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard

### Exercises: Level 2

1. Join A and B
1. Find A intersection B
1. Is A subset of B
1. Are A and B disjoint sets
1. Join A with B and B with A
1. What is the symmetric difference between A and B
1. Delete the sets completely

### Exercises: Level 3

1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
1. Explain the difference between the following data types: string, list, tuple and set
2. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
"""

# ========================
# Find the length of the set it_companies
# ========================
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies)) # 7

# ========================
# Add 'Twitter' to it_companies
# ========================

it_companies.add('Twitter')
it_companies.update('X')
print(it_companies)

# ========================
# Insert multiple IT companies at once to the set it_companies
# ========================

it_companies.update(['Red hat','TCS','Hotstar'])
print(it_companies)

# ========================
# Remove one of the companies from the set it_companies
# ========================

it_companies.remove('TCS')
print(it_companies,'\n')

# ========================
# What is the difference between remove and discard
# ========================
it_companies.discard('Apple')
print(it_companies)

# ========================
# Join A and B
# ========================

a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}

# c = a.union(b)
# print(c)
# a.update(b)
# print(a)

# ========================
# Find A intersection B
# ========================
d = a.intersection(b)
e = b.intersection(a)
print("Intersection: ", d)

# ========================
# Are A and B disjoint sets (If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.)
# ========================

boolData = a.isdisjoint(b)
if boolData is False:
    print('Yes, A and B is the disjoint sets')
else:
    print('Nope! They are not disjoint!')

# ========================
# Join A with B and B with A
# ========================
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
c = a.union(b)
f = b.union(a)
print(c)

# ========================
# What is the symmetric difference between A and B
# ========================

d = a.symmetric_difference(b)
print(d)

# ========================
# Delete the sets completely
# ========================

del a

# ========================
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# ========================
# List of ages
ages_list = [25, 30, 35, 25, 40, 30, 45]

# Convert the list to a set
ages_set = set(ages_list)

# Compare the length of the list and the set
if len(ages_list) > len(ages_set):
    print("The list is bigger.")
elif len(ages_list) < len(ages_set):
    print("The set is bigger.")
else:
    print("The list and the set have the same length.")

# ========================
# Explain the difference between the following data types: string, list, tuple and set
# ========================
"""
Strings are used to represent text data and are immutable.
Lists are ordered, mutable collections that allow duplicate elements.
Tuples are ordered, immutable collections often used for unchanging sequences of data.
Sets are unordered, mutable collections that store unique elements and are useful for mathematical operations like intersection and union.
"""


