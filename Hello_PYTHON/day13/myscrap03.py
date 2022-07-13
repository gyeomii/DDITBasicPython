import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)

if response.status_code == 200:
    html = response.content.decode('euc-kr','replace')
    soup = BeautifulSoup(html, 'html.parser')
    trArr = soup.select('tr')
    td = trArr[0].select('td')
    print(td[0].text)

else : 
    print(response.status_code)