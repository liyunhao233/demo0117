import os
import requests
from requests_toolbelt import MultipartEncoder
import tkinter as tk
from tkinter import filedialog


def upload_file(file_path):
    #file_path = "/path/demo.pdf"
    #file_path=r"C:\Users\Administrator\Desktop\桌面壁纸\1.jpg"
    file_size = os.path.getsize(file_path)
    url = "https://open.feishu.cn/open-apis/drive/v1/files/upload_all"
    form = {'file_name': 'Test0217.xlsx',
            'parent_type': 'explorer',
            'parent_node': '',
            'size': str(file_size),
            'file': (open(file_path, 'rb'))}
    multi_form = MultipartEncoder(form)
    headers = {
        'Authorization': 'Bearer '+"u-2gUFTNBMd49bTQIdQv_kH5hlhK5Q4lmxMo005gyGyeNc",  ## 获取tenant_access_token, 需要替换为实际的token
    }
    headers['Content-Type'] = multi_form.content_type
    response = requests.request("POST", url, headers=headers, data=multi_form)
    print(response.text)

def filetoken():
    url="https://open.feishu.cn/open-apis/drive/explorer/v2/root_folder/meta"

    headers = {
        'Authorization': 'Bearer ' + "t-g1042a8HNBCLAU6LE4CBYYHE4CS35GH3GDX5UYFE",
        ## 获取tenant_access_token, 需要替换为实际的token
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)

if __name__ == '__main__':
    # 实例化
    root = tk.Tk()
    root.withdraw()
    # 获取文件夹路径
    f_path = filedialog.askopenfilename(initialdir=r"\\192.168.2.100\100\版本迭代")
    print(f_path)
    upload_file(f_path)
    # filetoken()