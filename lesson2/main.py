import requests
import fake_useragent
from bs4 import BeautifulSoup

# получаем данные с сайта
link = 'https://browser-info.ru/'
response = requests.get(link).text

# создаём объект
soup = BeautifulSoup(response,'lxml')

# поиск блока
block = soup.find('div',id='tool_padding') # find() - поиск первого совпадения find_all() - поиск всех совпадений
#print(block)

# поиск javascript
check_js = block.find('div',id='javascript_check')
#print(check_js)

# result_js - включён ли js или нет
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'
print(result_js)

# проверяем flash
check_flash = block.find('div',id='flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'
print(result_flash)

# проверяем значение user-agent
check_user = block.find('div',id='user_agent').text
print(check_user) # User-agent: python-requests/2.24.0

# Многие сайты не принимают юзер агент python-requests.
# Следовательно необходимо подменять юзер агент

header = {'user-agent':'ddytfytdredxrg'}

link = 'https://browser-info.ru/'
response = requests.get(link,headers=header).text
soup = BeautifulSoup(response,'lxml')
block = soup.find('div',id='tool_padding')
check_user = block.find('div',id='user_agent').text
print(check_user)


# работа с модулем fake-useragent

user = fake_useragent.UserAgent().random # получаем случайный юзер-агент
header = {'user-agent':user}
link = 'https://browser-info.ru/'
response = requests.get(link,headers=header).text
soup = BeautifulSoup(response,'lxml')
block = soup.find('div',id='tool_padding')
check_user = block.find('div',id='user_agent').text
print(check_user)
