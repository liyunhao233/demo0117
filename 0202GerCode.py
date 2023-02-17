import requests
import json

url=""

payload = json.dumps({
     "code": "" #如何拿到？
})
headers = {
    'Content-Type': 'application/json;charset=utf-8'
}
response = requests.request("GET", url)
print(response.text)