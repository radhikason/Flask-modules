import requests
import json
url = "http://localhost:9000/api"
data = json.dumps({'sl':5.84,'sw':3.0, 'pl':3.75,'pw':1.1})

# r = requests.post(url, json = {'text': 'good'})
r = requests.post(url, data)
print(r.json())