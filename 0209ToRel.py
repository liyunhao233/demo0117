import requests
import json
import sys
import win32com.client
import GetToken
import win32api, win32con
import GetTenant_token
import datetime

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

    def getCell(self, sheet, row, col):  # 获取单元格的数据
        "Get value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row, col).Value

    # 下面是一些测试代码。
    def GetToken(self):
        print()


#  一定要是u_token 才能够创建  文档成功！！！
def post(PojName, u_token,parent_node_token):
    # win32api.MessageBox(0, "postfun", "node_token", win32con.MB_OK) #7188039318182002689
    url = "https://open.feishu.cn/open-apis/wiki/v2/spaces/7199517959354548252/nodes"  # 知识空间的id  需要在一开始就固定好
    payload = json.dumps({
        "node_type": "origin",
        "obj_type": "doc",
        "origin_node_token": "",
        "parent_node_token": parent_node_token,  # 创建大节点的，不需要token   后续字节点需要用到token
        "title": PojName + "发布成功！"+ dt
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + u_token  # token随时会变化
    }

    requests.request("POST", url, headers=headers, data=payload)

    '''xls = easyExcel(r'' + excelpath)
    xls.setCell('sheet1', 1, 3, node_token)
    xls.setCell('sheet1', 3, 3, id)
    #win32api.MessageBox(0, "zzz" + node_token, "excel", win32con.MB_OK)
    xls.save()
    xls.close()'''


def Get_parent(path):
    #win32api.MessageBox(0, 'intoget', "parent", win32con.MB_OK)
    xls = easyExcel(r'' + path)
    parent=xls.getCell('sheet1', 251, 2)
    #win32api.MessageBox(0, str(parent), "parent66", win32con.MB_OK)
    xls.save()
    xls.close()
    return str(parent)


def Get_UID(path):
    #win32api.MessageBox(0, 'intoget', "parent", win32con.MB_OK)
    xls = easyExcel(r'' + path)
    UID=xls.getCell('sheet1',252,2)
    #win32api.MessageBox(0, str(UID), "not str uid", win32con.MB_OK)
    xls.save()
    xls.close()
    return str(UID)

def SendRelMsg(t_token, idlist,pojname):
    url = "https://open.feishu.cn/open-apis/message/v4/batch_send/"
    #win32api.MessageBox(0, "SendMsg", "1", win32con.MB_OK)
    payload = json.dumps({
        "open_ids": idlist,
        "msg_type": "text",
        "content": {
            "text": "项目"+pojname+"发布成功！"
        }
    })
    headers = {
        'Authorization': 'Bearer ' + t_token,
        'Content-Type': 'application/json',
        # 'Cookie': 'QXV0aHpDb250ZXh0=87195dfb9647489d8c4d47501f02172f; _csrf_token=69a5d8caeab23edb41a4412c4193dd0d2d338823-1675148613; passport_web_did=7019866197608923137; swp_csrf_token=4c8ce1cd-4059-4bda-8ca6-78db31a8dd65; t_beda37=f4b531f3ce7d5526166cd93e93d0c7070114134f34ed5d141c0cb8b664eb5cdf'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text)
    win32api.MessageBox(0, "发送消息完成！", "Done!", win32con.MB_OK)

# list1[0]  #path
# list1[1]  #pojname
# list1[2]   code
dt = datetime.datetime.now().strftime('%m%d-%H:%M') #时间戳 0217-08:42

list1 = sys.argv[1].split('>')
path = list1[0]
#win32api.MessageBox(0, path+'.xlsx', "path", win32con.MB_OK)

pojname=list1[1]
#win32api.MessageBox(0,pojname, "pojname", win32con.MB_OK)

code = list1[2]
u_token = GetToken.token(code)
#win32api.MessageBox(0,u_token, "u_token", win32con.MB_OK)


path=path+'.xlsx'
parent_node_token = Get_parent(path) #拿到了parent
#win32api.MessageBox(0, parent_node_token, "parent_node_token", win32con.MB_OK)


post(pojname,u_token,parent_node_token)

idstr=Get_UID(path)
#idstr=list(idstr)
idstr=idstr[1:-1]  #切片 yyds
idstr=idstr.replace("'",'')
idstr=idstr.replace(" ",'')
idlist=idstr.split(",")
#win32api.MessageBox(0,str(idlist), "idlist", win32con.MB_OK)

t_token = GetTenant_token.Tenanttoken()
SendRelMsg(t_token,idlist,pojname)
#win32api.MessageBox(0, "postfun Done!", "1", win32con.MB_OK)