import requests
import json
import sys
import win32com.client


class Post:
    def post(self):

        Bigname = list1[0]
        url = "https://open.feishu.cn/open-apis/wiki/v2/spaces/7188039318182002689/nodes"  # 知识空间的id  需要在一开始就固定好
        payload = json.dumps({
            "node_type": "origin",
            "obj_type": "doc",
            "origin_node_token": "",
            "parent_node_token": "",  # 创建大节点的，不需要token   后续字节点需要用到token
            "title": PojName
        })

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer u-08wSadwft2SbcIeXE_WkbH055I2A05QFra00l4Uay1kG'  # token随时会变化
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        m = response.json()
        global node_token
        node_token = m['data']['node']['node_token']
        print(node_token)  # 将创建好的大节点放入excel中（模板中吗？） 可以


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

if __name__ == "__main__":


    list1 = sys.argv[1].split('>')
    #list1[2]
    PojName=list1[0]
    ExcelPath = list1[1]
    xls = easyExcel(r''+ExcelPath)
    xls.setCell('sheet1', 1, 3,node_token)
    print("*******beginsetCellformat********")
    xls.save()
    xls.close()
