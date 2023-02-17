import requests
import json
import datetime

def CreateWikiNode():

    url = "https://open.feishu.cn/open-apis/wiki/v2/spaces/"+sapce_id+"/nodes" #space id7188039318182002689
    payload = json.dumps({
	"node_type": "origin",
	"obj_type": "doc",
	"origin_node_token": "",
	"parent_node_token": "",
	"title": "2"
})
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer u-28IIsxdONaxqQHEKWJ7HjW055Iy405kxPG000gEay4hG'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

