import requests
from datetime import datetime
from bs4 import BeautifulSoup   
from day13.stockdao import StockDao

sd = StockDao()
ymd = datetime.today().strftime("%Y%m%d.%H%M")

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)

if response.status_code == 200:
    
    html = response.content.decode('euc-kr','replace')
    soup = BeautifulSoup(html, 'html.parser')
    
    attr1 = {'class' : 'st2', 'width' : '92'}
    
    tds = soup.find_all('td', attrs = attr1)
    #attr2 = {'width':'60'}
    #price = soup.find_all('td', attrs= attr2)
    
    count = 0
    for idx, td in enumerate(tds):
        s_code = td.a['title']
        s_name = td.text
        price = td.parent.find_all("td")[1].text.replace(",","")
        
        cnt = sd.insert(s_code, ymd, s_name, price)
        
        print(idx+1, "cnt", cnt)
        count += 1
        
    print(count, "개의 레코드가 입력되었습니다.")

else : 
    print(response.status_code)