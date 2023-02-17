import requests
import json

url = "https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri={https://open.feishu.cn/api-explorer/cli_a34a74d63a395013}&app_id={cli_a34a74d63a395013}"
payload = json.dumps({
	"node_type": "origin",
	"obj_type": "doc",
	"origin_node_token": "",
	"parent_node_token": "",
	"title": "21Test"
})


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer u-08wSadwft2SbcIeXE_WkbH055I2A05QFra00l4Uay1kG'
}

response = requests.request("GET", url)
print(response.text)