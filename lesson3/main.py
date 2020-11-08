import requests
import fake_useragent


session = requests.Session()
# используем сессию для сохранения куки файлов
user  = fake_useragent.UserAgent().random

link='http://ru-forum.com/login.php?action=in'

header = {'user-agent': user}

data ={
    'req_username':	"mytestusr",
    'req_password':'AVpIC4CT'

}

response =session.post(link,data=data,headers=header).text

profile_info = 'http://ru-forum.com/profile.php?id=2520'
profile_response = session.get(profile_info,headers= header).text
# работа с куки
cookies_dict = [
    {'domain': key.domain,'name':key.name,'path':key.path,'value':key.value}
    for key in session.cookies
]
# читаем куки
session2 = requests.Session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies)
profile_response2 = session2.get(profile_info,headers= header).text
print(profile_response2)