import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)

if response.status_code == 200:
    html = response.content.decode('euc-kr','replace')
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select('table')
    print(table)

else : 
    print(response.status_code)