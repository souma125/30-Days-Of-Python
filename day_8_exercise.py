person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['address']['job_title'] = 'Instructor'
print(person)
person['skills'].append('Python')

# Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'} 
print(dct.items(),'\n')

# Copy a Dictionary
newdict= person.copy() # newdict is not the same as person!
print(newdict)

#Getting Dictionary Keys as a List
print(newdict.keys(),'\n')

#Getting Dictionary Values as a List
print(newdict.values(),'\n')

"""
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
"""

# ========================
# Create an empty dictionary called dog
# ========================
dog = {}
print(type(dog),'\n')

# ========================
# Add name, color, breed, legs, age to the dog dictionary
# ========================

dog = {
    'name':'dog_ame',
    'color':'dg_color',
    'bread':'dog_bread',
    'leg':'dog_legs',
    'age': 45
}
print(dog,'\n')

dog['birthday']=200312

print("After append: ",dog,"\n")

# ========================
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# ========================

stu_dct = {
    'first_name' :'stu_first_name',
    'last_name' :'stu_last_name',
    'gender' :'stu_gender',
    'age' :31,
    'marital' :True,
    'country' :'India',
    'city' :'kolkata',
    'address' :'Mahisbathan',
    'skills':['Python','Django','Flask']
}

# ========================
# Get the length of the student dictionary
# ========================
stu_dict_len = len(stu_dct)
print('Length:', stu_dict_len , '\n')

# ========================
# Get the value of skills and check the data type, it should be a list)
# ========================
skills = stu_dct.get('skills')
print('\nSkills:', skills ,'Type:', type(skills))

# ========================
# Modify the skills values by adding one or two skills
# ========================
stu_dct['skills'].append('HTML')
stu_dct['skills'].append('Jquery')
print("\nModified Skills:",stu_dct["skills"])

# ========================
# Get the dictionary keys as a list
# ========================
key_as_lst = stu_dct.keys()
for key in key_as_lst:
    print (key + " - "+ str(type(key)))

# ========================
# Get the dictionary values as a list
# ========================
value_as_lst = stu_dct.values()
for val in value_as_lst:
    print ("Value is:" +str(val)+", Type:"+str(type(val)))

# ========================
# Change the dictionary to a list of tuples using items() method
# ========================
tupls = list(stu_dct.items())
print("\nTuple List:\n", tupls)

# ========================
# Delete one of the items in the dictionary
# ========================
del_one_item = stu_dct.pop('address')
print("Deleted Item:", del_one_item,"\n")

# ========================
# Delete one of the dictionaries
# ========================
del person

