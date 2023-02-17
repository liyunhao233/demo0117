import os
import requests
from requests_toolbelt import MultipartEncoder

def upload_file():
    file_path = "/path/demo.pdf"
    file_size = os.path.getsize(file_path)
    url = "https://open.feishu.cn/open-apis/drive/v1/files/upload_all"
    form = {'file_name': 'demo.pdf',
            'parent_type': 'explorer',
            'parent_node': 'fldbcO1UuPz8VwnpPx5a92abcef',
            'size': str(file_size),
            'file': (open(file_path, 'rb'))}
    multi_form = MultipartEncoder(form)
    headers = {
        'Authorization': 'Bearer t-e13d5ec1954e82e458f3ce04491c54ea8c9abcef',  ## 获取tenant_access_token, 需要替换为实际的token
    }
    headers['Content-Type'] = multi_form.content_type
    response = requests.request("POST", url, headers=headers, data=multi_form)

if __name__ == '__main__':
    upload_file()