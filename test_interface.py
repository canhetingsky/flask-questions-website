import requests
import json
url = 'http://localhost:5000/search/?q=%E5%8C%97%E4%BA%AC&time=10'
response = requests.get(url)
if (response.status_code == 200):   # ok
    text = response.text
    print(text)
    dic = json.loads(text)
    for k, v in dic.items():
    	print(k)
    	print(v)
url = 'http://localhost:5000/login/'
data = {'username':'132','password':'123'}
r =requests.post(url,data)
print(r)
print(r.text)
print(r.content)