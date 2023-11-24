def sum_of_five_nums(a,b,c,d,e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst))

args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers) 
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin,sw,nor,*rest = countries
print(fin,sw,nor,rest)
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct))

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs
print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one,*country_lst_two]
print(nordic_countries)

for index, i in enumerate(countries):
    print(f"{i} = {index}")

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f,v in zip(fruits,vegetables):
    fruits_and_veges.append({'fruit':f,'veg':v})

print(fruits_and_veges)
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries_1,es,ru=names
print(nordic_countries_1,es,ru)