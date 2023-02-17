'''import array

srt = [{"openId": "ou_be97a7e0be2b5b6afa8d1b028fc9c56f", "unionId": "on_13489d32e76ac89d40d32485ef8f4930",
        "avatarUrls": [
            "https://s1-imfile.feishucdn.com/static-resource/v1/v2_781c04e3-4126-4456-9f32-8d5acd2ef76g~?image_size=72x72&cut_type=&quality=&format=png&sticker_format=.webp",
            "https://s1-imfile.feishucdn.com/static-resource/v1/v2_781c04e3-4126-4456-9f32-8d5acd2ef76g~?image_size=240x240&cut_type=&quality=&format=png&sticker_format=.webp",
            "https://s1-imfile.feishucdn.com/static-resource/v1/v2_781c04e3-4126-4456-9f32-8d5acd2ef76g~?image_size=noop&cut_type=&quality=&format=png&sticker_format=.webp",
            "https://s3-imfile.feishucdn.com/static-resource/v1/v2_781c04e3-4126-4456-9f32-8d5acd2ef76g~?image_size=640x640&cut_type=&quality=&format=png&sticker_format=.webp"],
        "i18nNames": {"en_us": "", "ja_jp": "", "zh_cn": ""}, "name": "李云浩", "displayName": "李云浩",
        "i18nDisplayNames": {"en_us": "", "ja_jp": "", "zh_cn": ""}},
       {"openId": "ou_fb59ff250a8d4958e8ae911ac2fbb341", "unionId": "on_162dd048c0f7fbc1391ea1bb6a29486e",
        "avatarUrls": [
            "https://s1-imfile.feishucdn.com/static-resource/v1/v2_4a51123e-d6a9-4e5a-954b-4953d734e3ag~?image_size=72x72&cut_type=&quality=&format=png&sticker_format=.webp",
            "https://s3-imfile.feishucdn.com/static-resource/v1/v2_4a51123e-d6a9-4e5a-954b-4953d734e3ag~?image_size=240x240&cut_type=&quality=&format=png&sticker_format=.webp",
            "https://s3-imfile.feishucdn.com/static-resource/v1/v2_4a51123e-d6a9-4e5a-954b-4953d734e3ag~?image_size=noop&cut_type=&quality=&format=png&sticker_format=.webp",
            "https://s1-imfile.feishucdn.com/static-resource/v1/v2_4a51123e-d6a9-4e5a-954b-4953d734e3ag~?image_size=640x640&cut_type=&quality=&format=png&sticker_format=.webp"],
        "i18nNames": {"en_us": "", "ja_jp": "", "zh_cn": ""}, "name": "余君珩", "displayName": "余君珩",
        "i18nDisplayNames": {"en_us": "", "ja_jp": "", "zh_cn": ""}}]

list1=list(srt)
print(len(list1))
user_num=len(list1)
for i in range(user_num):
    print(list1[i]["openId"])
'''
import hashlib
import os

'''# 使用 md5 算法
m = hashlib.md5()
# 要计算的源数据必须是字节串格式
# 字符串对象需要encode转化为字节串对象
m.update("test123".encode())
# 产生哈希值对应的bytes对象
resultBytes = m.digest()
# 产生哈希值的十六进制表示
resultHex = m.hexdigest()
print(resultHex)'''
import hashlib
import sys
# 文件名称
#file_name = "C:\Users\Administrator\Desktop\个人文档\脚本编程\autoit产品属性卡-11(1)\v007_00_card_.xlsx"
# 读取文件


'''with open(file_name, 'rb') as fp:
    data = fp.read(file_name)
# 使用 md5 算法
file_md5= hashlib.md5(data).hexdigest()
print(file_md5)'''
'''import time
import datetime

t=time.time()
print(t)                       #原始时间数据
print(int(t))                  #秒级时间戳
print(int(round(t * 1000)))

dt = datetime.datetime.now().strftime('%m%d-%H:%M')
print(dt)'''
import tkinter as tk
from tkinter import filedialog

# 实例化
root = tk.Tk()
root.withdraw()
# 获取文件夹路径
f_path = filedialog.askopenfilename(initialdir=r"\\192.168.2.100\100\版本迭代")
print(f_path)


