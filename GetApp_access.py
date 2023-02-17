import requests
import json

def token():
    url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal"
    payload = json.dumps({
    "app_id": "cli_a3636c57f0e3100b",#正式 cli_a3636c57f0e3100b   #cli_a34a74d63a395013
    "app_secret": "4IYCWuOiuy8NT9AAM0nPhgRcOUiTf5eg"#正式 4IYCWuOiuy8NT9AAM0nPhgRcOUiTf5eg #5AxOX3OVfGE7DVV9IO6iIhPxv4HllErF
})

    headers = {
    'Content-Type': 'application/json;charset=utf-8'
}

    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)  #app_access_token 和 tenant_access_token 都会出现？？
    a=json.loads(response.text)

    #print(a["app_access_token"])
    app_access_token=a["app_access_token"]
    return app_access_token
