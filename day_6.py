"""
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
operator: to join two or more tuples and to create a new tuple
"""

lst_1 = [4,3,2,30,30,7]
lst_2 = []
for i in lst_1:
    if i == 30:
        lst_1.remove(i)
    else:
        lst_2.append(i)
print(lst_2)

lst_3 = [4,3,2,30,30,7]
i = 0
while i < len(lst_3):
    if lst_3[i] == 30:
        lst_3.pop(i)
    else:
        i += 1
print(lst_3)

# Creating a Tuple
# Empty tuple: Creating an empty tuple
empty_tpl = ()
empty_tpl = tuple()
tpl = ('item1,item2')
print(len(tpl))

# Accessing Tuple Items
print(tpl[0])

# Slicing tuples

tpl_1 = ('item1', 'item2', 'item3','item4')
all_item = tpl_1[:4]
last_two_items = tpl_1[-2:]
first_three_items = tpl_1[:3]
middle_two_items = tpl_1[1:3]
print('All items:', all_item,'\nLast Two Item:', last_two_items ,'\nFirst Three Items:', first_three_items,'\nMiddle two items: ', middle_two_items )

# Range of Negative Indexes
fruits = ('banana', 'orange', 'mango', 'lemon')
orange_mango = fruits[-3:-1]
print(orange_mango)

# Counting items inside a tuple using count method
fruit = ("apple", "mango","pineapple")
print("Number of mangos:", fruit.count('mango'))

# Changing Tuples to Lists
lst = list(fruit)
print (type(lst), type(fruit))

# Checking an Item in a Tuple
if 'applee' in fruit:
    print('Yes')
else:
    print('No')

# Joining Tuples
all_fruites = fruits + fruit
print(all_fruites)

# Deleting Tuples
tpl_2 = ('item1', 'item2', 'item3','item4')
del tpl_2

