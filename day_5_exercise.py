"""
### Exercises: Level 1

1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```
 Exercises: Level 2

1. The following is a list of 10 students ages:

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- Sort the list and find the min and max age
- Add the min age and the max age again to the list
- Find the median age (one middle item or two middle items divided by two)
- Find the average age (sum of all items divided by their number )
- Find the range of the ages (max minus min)
- Compare the value of (min - average) and (max - average), use _abs()_ method

1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
"""

# ========================
# Declare an empty list
# ========================
lst = []

# ========================
# Declare a list with more than 5 items
# ========================

lst = ['a','b','c','d','e','f']

# ========================
# Find the length of your list
# ========================

lst_len = len(lst)
print("The length of my list is:", lst_len,"items")

# ========================
# Get the first item, the middle item and the last item of the list
# ========================
first_item = lst[0]
mid_index = lst_len // 2
mid_item = lst[mid_index]
last_index = lst_len - 1
last_item = lst[last_index]
print('First Item:', first_item,'\nMiddle Item:', mid_item,"\nLast Item", last_item)

# ========================
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# ========================
mixed_data_types_lst = ['Parineeta', 17 , 2.00 , 'No', 'Gazole']
print(mixed_data_types_lst)

# ========================
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# ========================
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# ========================
# Print the list using print()
# ========================
print(it_companies)

# ========================
# Print the number of companies in the list
# ========================
number_of_companies = len(it_companies)
print("\nNumber Of Companies In The List: ", number_of_companies )

# ========================
# Print the first, middle and last company
# ========================
first_company= it_companies [0] # First Company Name Is Facebook
middle_company = it_companies[int(number_of_companies / 2)]
last_company = it_companies[-1]
print('\nFirst Company : ', first_company ,'\nMiddle Company :' , middle_company ,"\nLast Company :" , last_company)

# ========================
# Print the list after modifying one of the companies
# ========================
find_index = it_companies.index('Facebook')
it_companies[find_index] = 'Meta'
print("list after modifying one of the companies: ", it_companies)

# ========================
# Add an IT company to it_companies
# ========================
it_companies.append('Tesla')
print('\nit_companies After Adding Tesla : ', it_companies)
it_companies.insert(3,'TCS')
print('\nit_companies After Inserting TCS at index position three : ', it_companies)

# ========================
# Insert an IT company in the middle of the companies list
# ========================

company_mid_index = len(it_companies) // 2
it_companies.insert (company_mid_index,'infosys')
print(it_companies)

# ========================
# Change one of the it_companies names to uppercase (IBM excluded!)
# ========================
up_cs_letter = it_companies[0].upper()
print(up_cs_letter)

# ========================
# Join the it_companies with a string '#;  '
# ========================
joining_str = ' # '.join(it_companies)
print(joining_str + '\n')

# ========================
# Check if a certain company exists in the it_companies list.
# ========================

if 'Microsoft' in it_companies:
    print('Yes')
else:
    print('No')

# ========================
# Sort the list using sort() method / Reverse the list in descending order using reverse() method 
# ========================
it_companies.sort()
print("\nsorted list(ASC):", it_companies, "\n")
it_companies.sort(reverse=True)
print("sorted list(DESC)", it_companies,"\n")

# ========================
# Slice out the first 3 companies from the list
# ========================
sliced_list_1 = it_companies[:4]
print ("Sliced List:", sliced_list_1 ,"\n")

# ========================
# Slice out the last 3 companies from the list
# ========================
sliced_list_last = it_companies[:-3]
sliced_list_last_1 = it_companies[0:7]
print('Original List: ', it_companies , '\n')
print ('Last Sliced List:', sliced_list_last ,'\n')
print ('Last Sliced List 1:', sliced_list_last_1 ,'\n')

# ========================
# Slice out the middle IT company or companies from the list
# ========================
it_companies_1 = ['infosys', 'Tesla', 'TCS', 'Oracle', 'Microsoft', 'Meta', 'IBM', 'Google', 'Apple', 'Amazon']
number_of_companies = len(it_companies_1)
middle_element = it_companies_1[int(number_of_companies / 2)]
it_companies_1.remove(middle_element)
print(it_companies_1)

# ========================
# Remove the first IT company from the list
# ========================
print('Original List: ', it_companies_1 , '\n')
del_first_company = it_companies_1.pop(0)
print (f"First Company Deleted : {del_first_company}")
print('\nUpdated List', it_companies_1,'\n')

# ========================
# Remove the middle IT company or companies from the list
# ========================
it_companies_2 = ['infosys', 'Tesla', 'TCS', 'Oracle', 'Microsoft', 'Meta', 'IBM', 'Google', 'Apple', 'Amazon']
number_of_companies_2 = len(it_companies_2)
middle_element_2 = it_companies_2[int(number_of_companies_2 / 2)]
it_companies_2.remove(middle_element_2)
print(it_companies_2)

# ========================
# Remove the middle IT company or companies from the list
# ========================
it_companies_3 = ['infosys', 'Tesla', 'TCS', 'Oracle', 'Microsoft', 'Meta', 'IBM', 'Google', 'Apple', 'Amazon']
number_of_companies_3 = len(it_companies_3)
last_index = number_of_companies_3 - 1
print(it_companies_3)
print(last_index)

# ========================
# Remove all IT companies from the list
# ========================
it_companies_4 = ['infosys', 'Tesla', 'TCS', 'Oracle', 'Microsoft', 'Meta', 'IBM', 'Google', 'Apple', 'Amazon']
it_companies_4.clear()
print(it_companies_4)

# ========================
# Destroy the IT companies list
# ========================
it_companies_5 = ['infosys', 'Tesla', 'TCS', 'Oracle', 'Microsoft', 'Meta', 'IBM', 'Google', 'Apple', 'Amazon']
del it_companies_5

# ========================
# Join the following lists:
# ========================
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_list = front_end + back_end
print("Full List:", full_list, "\n")

# ========================
# Join the following lists using extend:
# ========================
front_end_1 = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end_2 = ['Node','Express', 'MongoDB']
front_end_1.extend(back_end_2)
print('Full List:', front_end_1,"\n")
full_stack = front_end_1.copy()
print(full_stack)

# ========================
# Sort the list and find the min and max age
# ========================

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list in ascending order
sorted_ages = sorted(ages)

# Find the minimum and maximum ages
min_age = sorted_ages[0]
max_age = sorted_ages[-1]

print("Sorted Ages:", sorted_ages)
print("Minimum Age:", min_age)
print("Maximum Age:", max_age)

# ========================
# list and find the min and max age withot using min and max function
# ========================
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age_1 = ages[0]
max_age_1 = ages[0]
for age in ages:
    if age < min_age_1:
        min_age_1 = age
    if age > max_age_1:
        max_age_1 = age
print("Minimum Age:", min_age_1)
print("Maximum Age:", max_age_1)

# ========================
# Add the min age and the max age again to the list
# ========================
ages.append(min_age_1)
ages.append(max_age_1)
print ("Ages after adding Min & Max", ages )

# ========================
# Find the median age (one middle item or two middle items divided by two)
# ========================

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sorted_ages = sorted(ages)
n = len(sorted_ages)
if n % 2 == 1:
    mid_index = int( n/2)
    median_age = sorted_ages[mid_index]
else:
    mid_index_1 = (n - 1) // 2
    mid_index_2 = n // 2
    median_age = (sorted_ages[mid_index_1] + sorted_ages[mid_index_2]) / 2
    # median_age=(sorted_ages[mid_index_1] + sorted_ages[mid_index_2]) / 2

print("Median Age:", int(median_age))

# ========================
# Find the average age (sum of all items divided by their number )
# ========================
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
result = 0
for i in ages:
    result += i
average_age = int(result / len(ages))
print('Average age: ',average_age)

# ========================
# Find the range of the ages (max minus min)
# ========================
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = ages[0]
max_age = ages[0]
for age in ages:
    if age < min_age:
        min_age = age
    if age > max_age:
        max_age = age
range_of_ages = max_age - min_age
print ('Range:',int(range_of_ages), 'years')

# ========================
# Compare the value of (min - average) and (max - average), use abs() method
# ========================
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
total_age  = 0
for age in ages:
    total_age += age

avg = total_age  / len(ages)
min_age = ages[0]
max_age = ages[0]
for i in ages:
    if i < min_age:
        min_age=i
    if i > max_age:
        max_age=i

min_diff = abs(min_age - avg)
max_diff = abs(max_age-avg)
print("Minimum Age Difference:", min_diff)
print("Maximum Age Difference:", max_diff)

# ========================
# Find the middle country(ies) in the countries list
# ========================
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil',
'Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros''Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','EastTimor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France',
'Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India''Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan''Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali''Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal''Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland''Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia''Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain','Sri Lanka''Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey''Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela''Vietnam','Yemen','Zambia','Zimbabwe',
];
cn_len = len(countries)

if cn_len % 2 == 1:
    middle_cn_index = (cn_len - 1) // 2
    middle_country = countries[middle_cn_index]
else:
    middle_cn_index_1 = (cn_len - 1) // 2
    middle_cn_index_2 =  cn_len // 2
    middle_country = (countries[middle_cn_index_1] + countries[middle_cn_index_2]) / 2

print('Middle Country is: ', middle_country, '\n')

# ========================
# Find the middle country(ies) in the countries list
# ========================

countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil',
'Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros''Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','EastTimor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France',
'Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India''Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan''Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali''Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal''Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland''Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia''Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain','Sri Lanka''Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey''Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela''Vietnam','Yemen','Zambia','Zimbabwe',
]; # List of countries omitted for brevity

cn_len = len(countries)
middle_index = cn_len // 2

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if cn_len % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else:
    first_half = countries[:middle_index + 1]
    second_half = countries[middle_index + 1:]

print("First Half:", first_half,'\n')
print("Second Half:", second_half,'\n')

# ========================
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
# ========================
countries_1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first,second,third,*rest = countries_1
print(f'The first element {first} \n')
print(f'the Second Element {second} \n')
print(f"the third element {third} \n")
for i in rest : print("\t",i,"\n")
