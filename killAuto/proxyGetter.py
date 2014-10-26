'''
Created on 2014-10-26

@author: ww
'''
import re
import time
import urllib

from fileNames import rawProxyFile
from proxyChecker import workProxy
from wwTools.fileTools import openFilesTodic, getArrDic, dicAdd, saveData,\
    getDicStr, openFileToDic, getDicArr, dicRemove, hasFile


def getProxy(count):
    url='http://www.cn379.cn/mo.php?sxb=&tqsl='+count+'&ports%5B%5D2=&ktip=&sxa=&radio=radio&submit=%CC%E1++%C8%A1'
    #url='http://www.cn379.cn/mo.php?sxb=&tqsl=25000&ports%5B%5D2=&ktip=&sxa=&radio=radio&submit=%CC%E1++%C8%A1'

    req=urllib.request.Request(url)
    response=urllib.request.urlopen(req)
    data=response.read().decode('gbk')
    #print(data)
    return data
def getProxys(txt):
    #print(txt)
    p=re.compile(r'>(.*?)<BR')
    msp=p.findall(txt)
    return msp

def getAndSave(count):
    txt=getProxy(count)
    tList=getProxys(txt)
    tDic=getArrDic(tList)
    global proxyDic
    addDic=dicRemove(tDic,proxyDic)
    proxyDic=dicAdd(proxyDic,tDic)
    saveData(getDicStr(proxyDic),todayFile())
    print("nowCount:",len(getDicArr(proxyDic)))
    
    addList=getDicArr(addDic)
    print("addCount:",len(addList))
    workProxy(addList)


def todayFile():
    return rawProxyFile()
def initMe():
    global proxyDic
    if hasFile(todayFile()):
        proxyDic=openFileToDic(todayFile())
    else:
        proxyDic={}

def workOnce():
    print("work")
    initMe()
    getAndSave("30000")

def work():
    cdTime=60*30
    while 1:
        try:
            workOnce()
            time.sleep(cdTime)
        except Exception as e:
            print(e)
            time.sleep(cdTime)
        
        
        
        
if __name__ == '__main__':
    work()
    #workOnce()
    pass
