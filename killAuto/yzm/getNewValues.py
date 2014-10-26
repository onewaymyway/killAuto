import urllib.parse
import urllib.request
import json
import time
import socket
import http.cookiejar
import random
import re


def getWeb():
    url='http://www.ss911.cn/pages/reg/regUser.aspx'
    req=urllib.request.Request(url)
    response=urllib.request.urlopen(req)
    data=response.read().decode('utf-8')
    print(data)
    return data

def getValues(txt):
    p=re.compile(r'input type="hidden" name="(.*?)" id="(.*?)" value="(.*?)" ')
    msp=p.findall(txt)
    data={}
    for kk in msp:
        print(kk)
        key=kk[0]
        value=kk[2]
        data[key]=value

    print(data)
    
def getHidden():
    txt=getWeb()
    getValues(txt)
    
#getHidden()
t=time.ctime()
print(t)
