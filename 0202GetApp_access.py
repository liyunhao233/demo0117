import requests
import json

url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal"
payload = json.dumps({
    "app_id": "cli_a34a74d63a395013",
    "app_secret": "5AxOX3OVfGE7DVV9IO6iIhPxv4HllErF"
})

headers = {
    'Content-Type': 'application/json;charset=utf-8'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)  #app_access_token 和 tenant_access_token 都会出现？？
