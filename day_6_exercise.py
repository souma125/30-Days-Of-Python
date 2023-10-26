"""
Exercises: Level 1

1. Create an empty tuple
2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

Exercises: Level 2

1. Unpack siblings and parents from family_members
1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
1. Slice out the first three items and the last three items from food_staff_lt list
1. Delete the food_staff_tp tuple completely
1. Check if an item exists in  tuple:

- Check if 'Estonia' is a nordic country
- Check if 'Iceland' is a nordic country

  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```
"""

# ========================
# Create an empty tuple / Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# ========================
sister_lst = ('a','b','c')
brother_lst = ('d','e','f')

# ========================
# Join brothers and sisters tuples and assign it to siblings
# ========================
siblings = sister_lst + brother_lst

# ========================
# How many siblings do you have?
# ========================

num_of_siblings = len(siblings)
print(num_of_siblings)

# ========================
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# ========================
family_members=('father','mother')+siblings
print(family_members)

# ========================
# Unpack siblings and parents from family_members
# ========================
parents = family_members[:2]
print(parents)
siblings = family_members[2:]
print(siblings)

# ========================
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# =======================
fruits = ('apple','orange')
vegetables = ('potato','pumpkin')
products = ('laptop','desktop')
food_stuff_tp = fruits + vegetables + products
print('Food stuff:', food_stuff_tp, '\nLength:',len(food_stuff_tp))

# ========================
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# =======================
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))
print(food_stuff_lt[0])

# ========================
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# =======================

mid_index = len(food_stuff_tp) // 2
mid_food_stuff = food_stuff_tp[mid_index]
print(mid_food_stuff)

# ========================
# Slice out the first three items and the last three items from food_staff_lt list
# =======================
first_three = food_stuff_tp[:3]
print(first_three)
last_three = food_stuff_tp[3:]
print(last_three)

# ========================
# Delete the food_staff_tp tuple completely
# =======================
del food_stuff_tp

# ========================
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# =======================

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('Yes')
else:
    print("No")
# ========================
if 'Iceland' in nordic_countries:
    print('Yes')
else:
    print("No")


