# ========================
# Iterate 0 to 10 using for loop, do the same using while loop.
# ========================
for i in range(11):
    print(i,end='\n')


j = 0
while j < 11:
    print(j,end='\n')
    j += 1

# ========================
# Iterate 10 to 0 using for loop, do the same using while loop.
# ========================
for a in range(10,-1,-1):
    print(a)

# ========================
# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
# ========================

for b in range(0,11):
    print('{} * {} = {}'.format(b,b,b * b))

# ========================
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# ========================
items = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in items:
    print(item,'\n')

# ========================
# Use for loop to iterate from 0 to 100 and print only even numbers
# ========================

for even_num in range(0,101):
    if even_num % 2 == 0:
        print('Even number: ',even_num,'\n')

# ========================
# Use for loop to iterate from 0 to 100 and print only odd numbers
# ========================

for odd_num in range(0,100):
    if odd_num % 2 != 0:
        print('Odd numbers: ', odd_num,'\n') 

# ========================
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# ========================

total = 0
for sum_num in range(0,101):
    total += sum_num
print('The sum of all numbers is: ', total, '\n')

# ========================
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# ========================

total_even = 0
total_odd = 0

for num in range(0,101):
    if num % 2 == 0:
        total_even += num
    if num % 2 != 0:
        total_odd += num
print('The sum of all evens is {}. And the sum of all odds is {}'.format(total_even,total_odd), '\n')

# ========================
# Go to the data folder and use the countries list. Loop through the countries and extract all the countries containing the word land
# ========================

countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil',
'Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros''Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','EastTimor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France',
'Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India''Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan''Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali''Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal''Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland''Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia''Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain','Sri Lanka''Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey''Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela''Vietnam','Yemen','Zambia','Zimbabwe',
]

for country in countries:
    if country.find('land') != -1:
        print('countries have "land" in their name: ',country,'\n')

# ========================
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# ========================
fruit_list=['banana','orange','mango','lemon']
new_fruit_list=[] #empty list that will store reversed elements
for fruit in range(len(fruit_list) -1,-1,-1):
    new_fruit_list.append(fruit_list[fruit])
print('Reversed fruit list: ',new_fruit_list, '\n')

# ========================
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world
# ========================
from countries_data import *
total_language = [] # list
most_spoken_languages = {} # dict
most_populated_countries = {}
for countries_data in countries_datas:
    # print(countries_data['languages'])
    for countries_data['language'] in countries_data['languages']:
        # if countries_data['language'] not in total_language:
        total_language.append(countries_data['language'])
    country_name = countries_data['name']
    country_population = countries_data['population']
    most_populated_countries[country_name] = country_population

number_of_languages = len(total_language)
# What are the total number of languages in the data
print("Total number of languages in the data : ", number_of_languages ,'\n')

# Find the ten most spoken languages from the data
for item in total_language:
    if item not in most_spoken_languages:
        most_spoken_languages[item] = 1
    else:
        most_spoken_languages[item] += 1

sorted_dict_most_spoken_languages = dict(sorted(most_spoken_languages.items(),key= lambda item:item[1],reverse=True))
for item, count  in sorted_dict_most_spoken_languages.items():
    print(f'{item}: {count}','\n')

# Find the 10 most populated countries in the world
print('Find the 10 most populated countries in the world','\n')
sorted_dict_most_populated_countries = sorted(most_populated_countries.items(),key= lambda item:item[1],reverse=True)
# Take the top 10 entries
# sorted_list_most_populated_countries = list(sorted_dict_most_populated_countries)
top_10_populated_countries = sorted_dict_most_populated_countries[:10]
for cn_name, cn_population in top_10_populated_countries:
    print(f'{cn_name}: {cn_population}','\n')



