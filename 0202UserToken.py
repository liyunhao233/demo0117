import requests
import json

url = "https://open.feishu.cn/open-apis/mina/v2/tokenLoginValidate"
payload = json.dumps({
     "code": "609f497c774387ca" #如何拿到？ 且只能使用一次！
})

headers = {
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization':'Bearer t-g10422eiZRLGXKQ35RJ4C4HE57VIAJKYTDQ4UILJ'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)  #app_access_token 和 tenant_access_token 都会出现？？
