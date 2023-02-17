import requests
import json
import GetApp_access

def token(code):
    url = "https://open.feishu.cn/open-apis/mina/v2/tokenLoginValidate"
    appaccesstoken = GetApp_access.token()
    payload = json.dumps({
        "code":str(code) # 如何拿到？ 且只能使用一次！
    })

    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': str(appaccesstoken)  # app_access_token 固定值 2小时有效值 需要重新获取
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)  # app_access_token 和 tenant_access_token 都会出现？？
   # print(response.text["data"])
    a=json.loads(response.text)
    #print(a["data"]["access_token"])
    accesstoken=a["data"]["access_token"]
    return accesstoken

