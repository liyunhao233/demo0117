import sys
import win32api,win32con
list1=sys.argv[1]
win32api.MessageBox(0,list1,"title",win32con.MB_OK)
win32api.MessageBox(0,'test',"mid",win32con.MB_OK)
