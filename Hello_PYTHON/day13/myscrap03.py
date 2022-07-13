import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)

if response.status_code == 200:
    html = response.content.decode('euc-kr','replace')
    soup = BeautifulSoup(html, 'html.parser')
    attr1 = {'class' : 'st2', 'width' : '92'}
    attr2 = {'width':'60'}
    name = soup.find_all('td', attrs = attr1)
    price = soup.find_all('td', attrs= attr2)
    for idx, nm in enumerate(name):
        print(idx, nm.text, price[idx].text)

else : 
    print(response.status_code)