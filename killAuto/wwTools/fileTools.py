"""Utility functions for copying and archiving files and directory trees.



"""
from datetime import datetime
import os
import shutil
import time


def getDicArr(dic):
    rst=[]
    for ct in dic:
        rst.append(ct)
    return rst

def getArrDic(arr):
    rst={}
    for ct in arr:
        rst[ct]=1
    return rst

def getArrStr(arr):
    return "\n".join(arr)

def getDicStr(dic):
    return getArrStr(getDicArr(dic))

def saveData(data,fname):
    f=open(fname,"w",encoding="utf-8");
    f.write(data)
    f.close()

def appendData(data,fname):
    f=open(fname,"a",encoding="utf-8");
    f.write(data)
    f.close()
    
def openFileToDic(of):
    if hasFile(of):
        pass
    else:
        print("warning file not found:",of)
        return {}
    f=open(of,"r",encoding="utf-8")
    lines=f.readlines()
    f.close()
    rst={}
    for line in lines:
        tline=line.strip()
        if len(tline)<1:
            continue
        if tline in rst:
            continue
        rst[tline]=1
    
    return rst

def openFilesTodic(fList):
    rst={}
    for tFile in fList:
        tCt=openFileToDic(tFile)
        rst=dicAdd(rst, tCt)
    return rst

def openFilesToArr(fList):
    rst=getDicArr(openFilesTodic(fList))
    return rst

def openFileToArr(of):
    return getDicArr(openFileToDic(of))

def dicRemove(oDic,rDic):
    rst={}
    for ct in oDic:
        if ct in rDic:
            pass
        else:
            rst[ct]=1
    return rst
def arrRemove(oarr,rarr):
    rstDic=dicRemove(getArrDic(oarr), getArrDic(rarr))
    return getDicArr(rstDic)
    
def dicAdd(oDic,rDic):
    rst={}
    for ct in oDic:
        rst[ct]=1
    for ct in rDic:
        rst[ct]=1
    return rst

def arrAdd(oarr,rarr):
    rstDic=dicAdd(getArrDic(oarr), getArrDic(rarr))
    return getDicArr(rstDic)

def getDateName():
    dt = datetime.now()
    rst=str(dt.strftime('%Y-%m-%d'))
    return rst

def copyFile(sFile,tFile):
    shutil.copy(sFile, tFile)  

def hasFile(file):
    return os.path.exists(file)
    

if __name__ == '__main__':
    print(getDateName())
    pass