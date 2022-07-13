import requests
 
URL = "http://127.0.0.1:5000/"
resp = requests.get(URL)
print(resp.status_code)
print(resp.text)