import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    trArr = soup.select('tr')
    for idx, tr in enumerate(trArr):
        if(idx > 0): 
            tdArr = tr.select('td')
            print(idx, tdArr[1].text, tdArr[3].text)

else : 
    print(response.status_code)