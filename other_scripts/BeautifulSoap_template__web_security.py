import requests
from bs4 import BeautifulSoup as Bs

#proxies = {'http': 'localhost:8080', 'http': 'localhost:8080'}
#headers = {'user-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0)Gecko/20100101 Firefox/91.0'}
res = requests.get('https://blabla/page.html')
print(res.text)

souped = Bs(res.text,'html.parser')
print(souped.find_all('div')[3])
