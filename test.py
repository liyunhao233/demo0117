import crypt
import json
import re
import requests
import win32api, win32con

a = {
    "code": 0,
    "data": {
        "node": {
            "creator": "ou_be97a7e0be2b5b6afa8d1b028fc9c56f",
            "has_child": False,
            "node_create_time": "1675837434",
            "node_token": "wikcnjcDUqKQj2TaEIeaV9ixtfO",
            "node_type": "origin",
            "obj_create_time": "1675837433",
            "obj_edit_time": "1675837434",
            "obj_token": "doccnViN6RwIaCsbNzONDQD1jkh",
            "obj_type": "doc",
            "origin_node_token": "wikcnjcDUqKQj2TaEIeaV9ixtfO",
            "origin_space_id": "7188039318182002689",
            "owner": "ou_be97a7e0be2b5b6afa8d1b028fc9c56f",
            "parent_node_token": "wikcnfKzJGgdo1ly4ywsry19Mfg",
            "space_id": "7188039318182002689",
            "title": "21Test"
        }
    },
    "msg": "success"
}
# m = a.json()
'''win32api.MessageBox(0, "test1"+str(a), "node_token", win32con.MB_OK)
node_token = a['data']['node']['node_token']
win32api.MessageBox(0, "test2"+node_token, "node_token", win32con.MB_OK)
print(node_token)'''


def SendMsg(id, t_token):
    url = "https://open.feishu.cn/open-apis/message/v4/batch_send/"

    payload = json.dumps({
        "open_ids": [
            id[0]
        ],
        "msg_type": "text",
        "content": {
            "text": "test content"
        }
    })
    headers = {
        'Authorization': 'Bearer ' + t_token,
        'Content-Type': 'application/json',
        # 'Cookie': 'QXV0aHpDb250ZXh0=87195dfb9647489d8c4d47501f02172f; _csrf_token=69a5d8caeab23edb41a4412c4193dd0d2d338823-1675148613; passport_web_did=7019866197608923137; swp_csrf_token=4c8ce1cd-4059-4bda-8ca6-78db31a8dd65; t_beda37=f4b531f3ce7d5526166cd93e93d0c7070114134f34ed5d141c0cb8b664eb5cdf'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


'''a = ["ou_be97a7e0be2b5b6afa8d1b028fc9c56f"]
print(a[0])
win32api.MessageBox(0,"a","b",win32con)'''


# SendMsg(a,"t-g10428gNBOKL7PTX5AMN2AAVRVVL5GX5CT26E6BZ")


def solo(t_token):
    url = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id"
    payload = json.dumps({
        "content": "{\"text\":\"?????????????????????\"}",
        "msg_type": "text",
        "receive_id": "ou_be97a7e0be2b5b6afa8d1b028fc9c56f",
        "uuid": ""
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + t_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


# solo("t-g10428gNBOKL7PTX5AMN2AAVRVVL5GX5CT26E6BZ")
'''ss = "'old','old','string'"
ret = ss.replace("'", '')
print(ret)'''

'''import os
path=r"\\192.168.2.100\100\????????????\v_v_a_??????01_??????\V000-202302091457_?????????\V000_202302091457_A00Card_?????????.xlsx"
a=os.path.getsize(path)
print(a)
b=open(path, 'rb')
print(b)'''

'''string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
print(string_list)
pattern = re.compile(r"The", re.I)
print(pattern)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output #38: {0:d}".format(4))'''''



'''import win32com.client as win32
#??????
xlApp = win32.Dispatch("Excel.Application")
#xlApp = win32.DispatchEx("Excel.Application")#???????????????????????????
#????????????, ?????????, ?????????
xlApp.Visible = 0;
xlApp.DisplayAlerts = 0;'''



'''FileName=r"C:\Users\Administrator\Desktop\????????????\????????????\autoit???????????????-11(1)\v007_00_card_.xlsx"
#??????????????????
xlBook = xlApp.Workbooks.Open(FileName)
#?????????????????????
new_xlBook = xlApp.Workbooks.Add()

#??????
xlSheet = xlBook.Worksheets('Sheet1')
a = xlSheet.Cells(1, 5).Value  # (row, col) ?????????1??????
print(a)
xlSheet.Cells(11, 5).Value = 2  # (row, col) ?????????1??????

#????????????
xlSheet.Range(xlSheet.Cells(11, 5), xlSheet.Cells(13, 6)).Value=6666

#????????????
#xlSheet.Shapes.AddPicture(picturename, 1, 1, Left, Top, Width, Height)

#copy ?????????
#xlSheet2.Copy(None, xlSheet)

#??????
#xlBook.SaveAs(FileName)#?????????
xlBook.Save()

#??????
xlBook.Close()
#xlBook.Quit()
'''

