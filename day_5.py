"""
Lists
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.
"""

#=============================
# How to Create a List
# In Python we can create lists in two ways:
#==============================

# Using list built-in function

lst = list()
empty_list = list()
print(len(empty_list))

# Using square brackets, []
lst_1 = []
print("Length of lst:", len(lst), "and length of empty list")

# Lists with initial values. We use len() to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Fruits: ', fruits)
print('Number of fruits are: ', len(fruits))

# Lists can have items of different data types
lst_2 = ['Asabeneh',250,True,{'country':'Finland', 'city':'Helsinki'}]

# Accessing List Items Using Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
print("\nAccessing elements using positive indexing:", fruits[0])  # Note that index starts from zero!
last_index = len(fruits) - 1
last_fruits = fruits[last_index]
print('\nLast element:', last_fruits )

# Accessing List Items Using Negative Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]   ## This will print out mango because it's at position (-3) counting backwards starting from end
second_fruit = fruits[-3]   # The second argument indicates position from end so it will return banana here
print(second_fruit)

# Unpacking List Items
lst_3 = ['item1','item2','item3', 'item4', 'item5']

first_ele,second_ele,*rest = lst_3
print(first_ele)
print(second_ele)
print(rest)

# Second Example about unpacking list
first,second,third,*rest,tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

# Slicing Items from a List
fruits=['apple','banana','cherry','durian','elderberry']
print(fruits[:],'\n')     # This is called slicing and gives all the fruit names in this order
all_fruits = fruits[0:5]
print(all_fruits,'\n')
all_fruits_1 = fruits[0:]
print(all_fruits_1,'\n')
banana_and_durian = fruits[1:4]
print(banana_and_durian,'\n')
banana_mango_elderberry = fruits[1:]
print(banana_mango_elderberry,'\n')
banana_durian = fruits[1:3]
print("Every other item starting at first item",banana_durian,"\n")
banana_elderberry = fruits[1::3]
print("every third item starting with first one ",banana_elderberry," \n ")
durian_elderberry = fruits[3:]
print('from fourth to last ', durian_elderberry , " \n ")
elderberry_apple = fruits[-1::-4]
print ("From last till first", elderberry_apple ," \n ")
banana_apple = fruits[1::-1]
print ('Reverse of above example', banana_apple ,' \n ')
cherry_banana = fruits[2:0:-1]
print ( cherry_banana ,' \n ')
durian_cherry = fruits[3:1:-1]
print  ( durian_cherry ,' \n ')

# Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
fruits_1 = ['banana', 'orange', 'mango', 'lemon']
all_fruits_2 = fruits_1[-4:]
print(all_fruits_2,'\n')
orange_and_mango = fruits_1[-3:-1]
print(orange_and_mango,'\n')
orange_mango_lemon = fruits_1[-3:]
print(orange_mango_lemon,'\n')
reverse_fruit = fruits_1[::-1]
print(reverse_fruit,'\n')

# Modifying Lists (List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.)
fruits= ['apple','banana','cherry','durian','elderberry']
fruits[0]='pineapple'    # We can change an element by referring its index number
print(fruits,'\n')        # The changed value will reflect everywhere where it has been used previously as well
last_index_1 = len(fruits) - 1
fruits[last_index_1]='lime'
print(fruits, '\n')

# Checking Items in a List
if 'pineapple' in fruits:
    print("'pineapple' found!")
else:
    print("'pineapple' not found.")

# Adding Items to a List
fruits.append('apple')
print(fruits,'\n')

# Inserting Items into a List (We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.)

fruits.insert(2,'apple')
print(fruits,'\n')

# Removing Items from a List
lst_4 = ['item1', 'item2']
lst_4.remove('item1')
print(lst_4,'\n')

# Removing Items Using Pop
lst_5=['a','b','c','d','e']   ## lst_5=[a, b , c ]
removedItem = lst_5.pop()     ### removed item will be e and now lst_5 becomes [a, b, c]
print("Removed Item:",removedItem,"New List :",lst_5,"\n")
removedItem_1 = lst_5.pop(0)
print ("Removed Item:" + str(removedItem_1)+ " New List :" +str(lst_5)+"\n" )

# Removing Items Using Del
del lst_5[0]
print(lst_5,'\n')

#Copying a List
fruits_copy = fruits.copy()
print(fruits_copy,'\n')

# Joining Lists
positive_numbers = [1, 2, 3, 4, 5]
negative_numbers = [-5,-4,-3,-2,-1]
alNumbers = positive_numbers + negative_numbers
print(alNumbers,'\n')

# Joining using extend() method The extend() method allows to append list in a list. See the example below.

lst_6 = ['item1', 'item2']
lst_7 = ['item3', 'item4', 'item5','item']
lst_6.extend(lst_7)
print (lst_6,'\n')

# Counting Items in a List

print ('The count of \'item\' is:',lst_7.count('item')) # Returns number of times an element occurs in a list

# Finding Index of an Item
print(lst_7.index('item'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

# Sorting List Items
ages.reverse()
print(ages)

ages.sort() # ascending
print(ages)
ages.sort(reverse=True) # descending
print(ages)