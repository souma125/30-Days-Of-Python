# ========================
# Short Hand
# ========================
a = -3
print('A is positive') if a > 0 else print('A is negative')

# ========================
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
# ========================

# age = int(input('Enter your age: '))
age = 18
age_diff = 0
if age >= 18:
    print('You are old enough to drive')
else:
    age_diff = 18 - age
    print(f'You need {age_diff} more years to learn to drive', age_diff)

# ========================
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
# ========================
# your_age = int(input('Enter your age: '))
your_age = 27
my_age = 31
# age_diff_2 = my_age - your_age
# print("You're", age_diff, "years younger")
if your_age == my_age:
    print("you are the same as me!")  # this will not work!
elif my_age >= your_age:
    print('I am {} {} younger than you'.format(abs(your_age-my_age), 'year'))
elif my_age <= your_age:
    print('I am {} {} older than you'.format(your_age-my_age, 'years'))
else:
    print('Invalid age')


# ========================
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# ========================

# numOne=int(input('Enter first number : '))
# numTwo=int(input('Enter second Number : '))
numOne = 4
numTwo = 3
if numOne > numTwo:
    print(numOne)
elif numOne < numTwo:
    print(numTwo)
elif numOne == numTwo:
    print(f'{numOne} is equal to {numTwo}', '\n')

# ========================
# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
# ========================

# stu_mark = int(input('Enter your suject mark: '))
stu_mark = 95
if stu_mark >= 80 and stu_mark <= 100:
    print('Your Grade is A')
elif stu_mark >= 70 and stu_mark <= 89:
    print('Your Grade is B')
elif stu_mark >= 60 and stu_mark <= 69:
    print('Your Grade is C')
elif stu_mark >= 50 and stu_mark <= 59:
    print('Your Grade is D')
elif stu_mark >= 0 and stu_mark <= 49:
    print('Your Grade is F')
else:
    print("Please enter valid marks")

# ========================
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# ========================

# month = input('Enter the month to know the season: ')
month = 'September'
print(month.capitalize())
if month.capitalize() == 'September' or month.capitalize() == 'October' or month.capitalize() == 'November':
    print('The season is Winter')
elif month.capitalize() == 'May' or month.capitalize() == 'March' or month.capitalize() == 'April':
    print('the season is Spring')
elif month.capitalize() == 'June' or month.capitalize() == 'July' or month.capitalize() == 'August':
    print('The season is Summer')
else:
    print('Invalid Month')

# ========================
# The following list contains some fruits:If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# ========================
fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit_name = input('Enter the fruit name: ')
fruit_name = 'pumpkin'
if fruit_name not in fruits:
    fruits.append(fruit_name)
print(fruits)

# ========================
# Here we have a person dictionary. Feel free to modify it!
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
# ========================

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

middleSkill = ''
if "skills" in person: # check if there are any skills listed for this person
    middleSkill = len(person['skills']) // 2
    print(person['skills'][middleSkill])
else:
    print('key error')

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Person know Python")
    else:
        print("Person don't know Python")
else:
    print('Key Error')

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if 'JavaScript' in person['skills']:
    if 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('He is just a frontend developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB'in person['skills']:
    print ('He is a backend developer')
else:
    print ("Not sure what kind of developer he is.")

#  If the person is married and if he lives in Finland, print the information in the following format:  Asabeneh Yetayeh lives in Finland. He is married.

if person['is_marred']  == True:
    if person['country'] == 'Finland':
        print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")
    else:
        print ( f'{person["first_name"]} {person["last_name"]}, you can not marry someone from another country.')
else:
    print (f'{person["first_name"]} {person["last_name"]} is not married')