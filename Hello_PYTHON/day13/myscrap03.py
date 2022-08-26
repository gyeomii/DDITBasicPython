import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)

if response.status_code == 200:
    html = response.content.decode('euc-kr','replace')
    soup = BeautifulSoup(html, 'html.parser')
    attr1 = {'class' : 'st2', 'width' : '92'}
    tds = soup.find_all('td', attrs = attr1)
    #attr2 = {'width':'60'}
    #price = soup.find_all('td', attrs= attr2)
    for idx, td in enumerate(tds):
        s_name = td.text
        s_price = td.parent.find_all("td")[1].text
        s_code = td.a['title']
        print(idx, s_code, s_name, s_price)

else : 
    print(response.status_code)