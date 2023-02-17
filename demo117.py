import  os
import sys
import win32api,win32con
#能调用网络盘的exe


#os.startfile(r"\\192.168.2.100\100\Demo0109.exe")
#print(sys.argv[1])

#list1=sys.argv[1].split(' ')
list1=sys.argv[1].split('>')
win32api.MessageBox(0,list1[0],"title",win32con.MB_OK)
win32api.MessageBox(0,sys.argv[1],"mid",win32con.MB_OK)
win32api.MessageBox(0,list1[1],"title2",win32con.MB_OK)



