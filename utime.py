import time
import datetime
import os
import re
x = -1 #初始化顺序次数
y =  y - 1
test = 'helloworld'
def changename():
    os.system('cd cex.bat')
def readname():
    filePath = fpath
    name = os.listdir(filePath)
    return name
i = readname()
def getname(x):
    if x > y:
        x = 0
    floatnm = float(i[x])
    floatnum = floatnm // 1000
    intname = int(floatnum)
    return intname
def rename():
    while x <= y:
        x = x + 1
        stt = x + 1
        result = getname(x)
        changed = datetime.datetime.fromtimestamp(result)
        src = str(result)
        src = src.replace(":","：")
        src = src.replace(" ","")
        dst = str(changed)
        dst = dst.replace(":","：")
        dst = dst.replace(" ","")
        last = 'rename ' + fpath + src + ' ' + dst + '.jpg' +'\n'
        f = open(temppath , "a+")
        f.write(last)
        f.close()
def atlast():
    last1 = 'move ' + temppath + " " + fpath
    last2 = fpath + 'click.bat'
    os.system(last1)
    os.system(last2)
    print("程序已完成，您可以打开放文件的目录查看效果，多出来的click.bat可以删除")
