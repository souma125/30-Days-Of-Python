# https://www.geeksforgeeks.org/python-web-scraping-tutorial/
import requests
from bs4 import BeautifulSoup
url = 'https://www.geeksforgeeks.org/python-programming-language/'
response = requests.get(url)
status = response.status_code
content = response.content
soup = BeautifulSoup(content,'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)
s = soup.find('div',class_='page_content')
content_1 = s.find_all('p')
for line in content_1: 
    # print(line.text)
    pass

for link in s.find_all('a'):
    # print(link.get('href'))
    pass

image_list = []
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt') 
    image_list.append({'src':src,'alt':alt})
for image in image_list:
    print(image)