import requests
import json

def Tenanttoken():
    url = "	https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = json.dumps({
    "app_id": "cli_a3636c57f0e3100b",  #new cli_a3636c57f0e3100b
    "app_secret": "4IYCWuOiuy8NT9AAM0nPhgRcOUiTf5eg"  #new 4IYCWuOiuy8NT9AAM0nPhgRcOUiTf5eg
})

    headers = {
    'Content-Type': 'application/json;charset=utf-8'
}

    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)  #app_access_token 和 tenant_access_token 都会出现？？
    a=json.loads(response.text)

    #print(a["tenant_access_token"])
    tenant_access_token=a["tenant_access_token"]
    return tenant_access_token

