# f = open('/30-Days-Of-Python/file/reading_file_example.txt')
# # txt = f.read()
# # print(txt)
# print(f.readline())
# print(f.readlines())
# f.close()

# with open('/30-Days-Of-Python/file/reading_file_example.txt') as f_1:
#     lines = f_1.read().splitlines()
#     print(lines)

# with open('/30-Days-Of-Python/file/reading_file_example.txt','a') as f_2:
#     f_2.write('This text has to be appended at the end') 

# import os
# # if os.path.exists('/30-Days-Of-Python/file/reading_file_example.txt'):
# #     os.remove('/30-Days-Of-Python/file/reading_file_example.txt')
# # else:
# #     print('Path not exists')

# import json
# person_json = '''{
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }'''

# person_dct = json.loads(person_json)
# print(person_dct['name'],end='\n')

# person = {
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }

# person_json = json.dumps(person)
# print(person_json,end="\n")
# import csv
# with open('/30-Days-Of-Python/file/csv_example.csv') as f:
#     csv_reader = csv.reader(f,delimiter=',')
#     line_count = 0
#     print()
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Columns names are: {", ".join(row)}',end='\n')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} is teacher. He lives in {row[1]},{row[2]}',end='\n')
#             line_count += 1

#     print(f'Number of lines are: {line_count}',end='\n')


# =============================================================================
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words 
# =============================================================================

with open('/30-Days-Of-Python/file/obama_speech.txt') as obama:
    content = obama.read()
    num_lines = len(content.splitlines())
    num_words = len(content.split())
    print(f'Number of lines: {num_lines}',end='\n')
    print(f'Number of words: {num_words}',end='\n')
    print()

# =============================================================================
# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
# =============================================================================
file_path = '/30-Days-Of-Python/file/countries_data.json'
number_of_records = 10
import json
total_language = [] #list
most_spoken_languages = {} #dict
item = []
most_populated_countries = {}
with open('/30-Days-Of-Python/file/countries_data.json',encoding='utf-8') as fp:
    data = fp.read()
    countries_lists = json.loads(data)
    # print(countries_lists)
    for countries_list in  countries_lists:
       for countries_list['language'] in countries_list['languages']:
           total_language.append(countries_list['language'])
       country_name = countries_list['name']
       country_population = countries_list['population']
       most_populated_countries[country_name] = country_population
    for item in total_language:
        if item not in most_spoken_languages:
            most_spoken_languages[item] = 1
        else:
            most_spoken_languages[item] += 1
            
    sorted_dict_most_spoken_languages = sorted(most_spoken_languages.items(),key= lambda item:item[1],reverse=True)
    top_ten_most_spoken_language = dict(sorted_dict_most_spoken_languages[:number_of_records])
    for item_1,count in top_ten_most_spoken_language.items():
        # print(f'{item_1}: {count}',end='\n')
        pass

# =============================================================================
#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
# =============================================================================
sorted_dict_most_populated_countries = sorted(most_populated_countries.items(),key= lambda item:item[1],reverse=True)
top_10_populated_countries = sorted_dict_most_populated_countries[:number_of_records]
for cn_name,cn_population in top_10_populated_countries:
     print(f'{cn_name}: {cn_population}','\n')