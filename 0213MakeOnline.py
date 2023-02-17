import requests
import json
import sys
import win32com.client
import GetToken
import win32api, win32con
import GetTenant_token


def SendMsg(t_token, idstr):
    url = "	https://open.feishu.cn/open-apis/message/v4/batch_send/"
    #win32api.MessageBox(0, "SendMsg", "1", win32con.MB_OK)
    payload = json.dumps({
        "open_ids": idstr,
        "msg_type": "text",
        "content": {
            "text": "新项目创建成功！"
        }
    })
    headers = {
        'Authorization': 'Bearer ' + t_token,
        'Content-Type': 'application/json',
        # 'Cookie': 'QXV0aHpDb250ZXh0=87195dfb9647489d8c4d47501f02172f; _csrf_token=69a5d8caeab23edb41a4412c4193dd0d2d338823-1675148613; passport_web_did=7019866197608923137; swp_csrf_token=4c8ce1cd-4059-4bda-8ca6-78db31a8dd65; t_beda37=f4b531f3ce7d5526166cd93e93d0c7070114134f34ed5d141c0cb8b664eb5cdf'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    win32api.MessageBox(0, "SendMsg", "2", win32con.MB_OK)

def post(PojName, u_token, excelpath,id):
    #win32api.MessageBox(0, "postfun", "node_token", win32con.MB_OK)#old id 7188039318182002689  new 7199517959354548252
    url = "https://open.feishu.cn/open-apis/wiki/v2/spaces/7199517959354548252/nodes"  # 知识空间的id  需要在一开始就固定好
    payload = json.dumps({
        "node_type": "origin",
        "obj_type": "doc",
        "origin_node_token": "",
        "parent_node_token": "",  # 创建大节点的，不需要token   后续字节点需要用到token
        "title": PojName
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + u_token  # token随时会变化
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    #win32api.MessageBox(0, "test1"+u_token, "node_token", win32con.MB_OK)
    a = json.loads(response.text)

    #win32api.MessageBox(0, "test2"+str(a), "node_token", win32con.MB_OK)
    node_token = a['data']['node']['node_token']

    xls = easyExcel(r'' + excelpath)
    xls.setCell('sheet1', 251, 2, node_token) #项目文件夹token位置
    xls.setCell('sheet1', 252, 2, str(id))  #项目人员ID
    #win32api.MessageBox(0, "zzz" + node_token, "excel", win32con.MB_OK)
    xls.save()
    xls.close()

    #win32api.MessageBox(0, "test3"+node_token, "node_token", win32con.MB_OK)
    # print(node_token)  # 将创建好的大节点放入excel中（模板中吗？） 可以

    #win32api.MessageBox(0, "test4", "node_token", win32con.MB_OK)


class easyExcel:

    def __init__(self, filename=None):  # 打开文件或者新建文件（如果不存在的话）
        self.xlApp = win32com.client.Dispatch('Excel.Application')
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ''

    def save(self, newfilename=None):  # 保存文件
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()

    def close(self):  # 关闭文件
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp

    def setCell(self, sheet, row, col, value):  # 设置单元格的数据
        "set value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Value = value

    # 下面是一些测试代码。
    def GetToken(self):
        print()


list1 = sys.argv[1].split('>')  # 会分出两个str  path codeandid（这个还需要分 通过 *）

# list1[1]    #网络盘文件夹路径
# list1[2]    #code
#win32api.MessageBox(0, list1, "list", win32con.MB_OK)
codeandid = list1[2].split('*')
#win32api.MessageBox(0, str(codeandid), "codeandid", win32con.MB_OK)
# openid = codeandid[1]
code = codeandid[0]
#win32api.MessageBox(0, str(code), "code", win32con.MB_OK)
u_token = GetToken.token(code)


#for i in range(len(codeandid) - 1):
    #id += codeandid[i + 1] + ','  # 实际选择人数
    #win32api.MessageBox(0, id, "id=====", win32con.MB_OK)

# win32api.MessageBox(0, str(codeandid), "codeandid=====", win32con.MB_OK)




#win32api.MessageBox(0, str(u_token), "u_token", win32con.MB_OK)

PojName = list1[0]  # 知识库文件名字
#win32api.MessageBox(0, str(PojName), "PojName", win32con.MB_OK)

excelpath = list1[1]
#win32api.MessageBox(0, str(excelpath), "excelpath", win32con.MB_OK)
del codeandid[0]
idlist=codeandid
post(PojName, u_token, excelpath,idlist)

t_token = GetTenant_token.Tenanttoken()
#win32api.MessageBox(0, str(t_token), "t_token", win32con.MB_OK)


#win32api.MessageBox(0, str(idlist), "str(idlist)", win32con.MB_OK)
#win32api.MessageBox(0, "IntoSendMsg", "v", win32con.MB_OK)
SendMsg(t_token,idlist)
#win32api.MessageBox(0, "SendMsgDone", "excelpath", win32con.MB_OK)
'''
    ExcelPath = list1[1]
    xls = easyExcel(r''+ExcelPath)
    xls.setCell('sheet1', 1, 3,node_token)
    print("*******beginsetCellformat********")
    xls.save()
    xls.close()
    '''
