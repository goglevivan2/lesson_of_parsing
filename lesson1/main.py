### ВВЕДЕНИЕ В REQUESTS

import requests

link = 'http://icanhazip.com/'
response=requests.get(link)
print(response.status_code)
print(response.text) # text - получаем html код со страницы, content - получаем байты со страницы


link = 'https://browser-info.ru/'

response = requests.get(link).text
print(response)

with open('1.html','w',encoding='utf-8') as file:
    file.write(response)