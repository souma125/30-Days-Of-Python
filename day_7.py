"""
Sets
Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
"""
# Creating a Set
st = set()

# Creating a set with initial items
st_1 = {'item1','item2'}

# Getting Set's Length
print(len(st_1))

# Accessing Items in a Set
print('does set st contain iteam1: ', 'item1' in st_1)
print('does set st contain item3: ', 'item3' in st_1)

# Adding Items to a Set
st_1.add('item3')
print('\nset after adding an element:', st_1)  # note the change of order when printing sets, as they are unordered data structures!

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.

st_1.update(['item4','item5','item6'])
print('\nset after adding multiple element:', st_1)

# Removing Items from a Set
st_1.remove('item6')
print('\nset after removing an element:', st_1)

# Clearing Items in a Set

st_2 = {'item1', 'item2', 'item3', 'item4'}
st_2.clear()

# Deleting a Set
del st_2

# Converting List to Set
lst_1 = ['item4','item5','item6']
st_3 = set(lst_1)
print(type(st_3))

# Joining Sets =>We can join two sets using the union() or update() method.(Union This method returns a new set)
s1= {0, 1}
s2={-7,-8,'a'}
s3 = s1.union(s2)
print("Union of two sets:",s3 ,'\n')

# Update This method inserts a set into a given set
s1.update([9]) # add new elements
print ("Updated set : ",s1, '\n')
s1.update(s2)
print ('updated again using union function: ', s1, '\n')

# Finding Intersection Items (Intersection returns a set of items which are in both the sets. See the example)

s4 = {1,2,3,4}
s5 = {1,8,4,7}
s6 = s4.intersection(s5)
print("Intersection of Two Sets",s6 , '\n')

# Checking the Difference Between Two Sets (It returns the difference between two sets.)

s7 = s4.difference(s5)
print("Difference between two sets: ",s7, "\n")

# Finding Symmetric Difference Between Two Sets
# (It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A))

s8 = s4.symmetric_difference(s5)
print(s8)

