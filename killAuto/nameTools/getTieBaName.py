import re
import urllib.parse
import urllib.request
import http.cookiejar
import json
import time
import socket

socket.setdefaulttimeout(8.0)
headers = {
    #'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Host': 'www.oicq88.com',
    #'Origin': 'http://www.ss911.cn',
    #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection' : 'keep-alive',
    'Cookie' : 'kutongji_sid29=70ae1e8a-f7b5-1718-ad29-01f9fea1228d; bdshare_firstime=1409210071967; BAIDU_DUP_lcr=http://www.baidu.com/s?wd=qq%E7%BD%91%E5%90%8D%E5%A4%A7%E5%85%A8&rsv_spt=1&issp=1&f=8&rsv_bp=0&ie=utf-8&tn=baiduhome_pg&bs=qq%E7%BD%91%E5%90%8D; kutongji_visit29=2; kutongji_sin29=; CNZZDATA1000000816=520869402-1409209824-http%253A%252F%252Fwww.baidu.com%252F%7C1412495879; kutongji_last29=1412496091',
    #'Cookie' : 'RK=J5FrJKalWu; pt2gguin=o0484641127; ptcz=e9fe4398eb29335c4dd918e3326fc04dd2e294f2a7331a7abd6f39bd5faeee92; pgv_pvid=2092053654; o_cookie=484641127; uin=o484641127; skey=ZzqCm70ICM; itkn=1928745486',
    'Pragma' : 'no-cache',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153'
            }
cj = http.cookiejar.CookieJar()
#tProxy="122.232.226.195:80"
#tProxy="127.0.0.1:8080"
iprecord=0
#proxy_handler = urllib.request.ProxyHandler({'http':tProxy})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

proxyList=[]

def getProxyTxt():
    f=open("pdata.txt","r",encoding="utf-8");
    txt=f.read();
    f.close()
    return txt
def getProxyHttp(url):
    req=urllib.request.Request(url)
    cdata=opener.open(req).read()
    #print(cdata)
    data=cdata.decode('gbk')
    return data

def addName(name):
    global nameDic
    global allDic
    if name in allDic:
        pass
    else:
        nameDic[name]=1
        allDic[name]=1
    

def getProxyList(pTxt):
    #pre=re.compile(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>whois</td><td><div class="addr_style">(.*?)</div></td></tr>')
    pre=re.compile(r"data-field='(.*?)'")
    #print(pTxt)

    matches=pre.findall(pTxt)

    nameSign=[
        "un",
        "author_name"
        ]
    #print(matches)

    for tP in matches:
        tP=tP.replace("&quot;",'"')
        #print(tP)
        data=json.loads(tP)
        for sign in nameSign:
            if sign in data:
                addName(data[sign])
        
        #print(data)
        

def saveData(data,fname):
    f=open(fname,"w",encoding="utf-8");
    f.write(data)
    f.close()

def appendData(data,fname):
    f=open(fname,"a",encoding="utf-8");
    f.write(data)
    f.close()

def getDicArr(dic):
    rst=[]
    for ct in dic:
        rst.append(ct)
    return rst

def getDataOnce():

    global nameDic
    nameDic={}
    rst=getProxyHttp('http://tieba.baidu.com/f?kw=%C4%A7%CA%DE%CA%C0%BD%E7')
    #print(rst)
    getProxyList(rst)
    #saveData(rst,"tb.txt")

    nameList=getDicArr(nameDic)
    nameStr="\n".join(nameList)
    print('Add:',len(nameList))
    print(nameStr)
    nameStr=nameStr+"\n"
    appendData(nameStr,"tbName.txt")
    
def initNameDic(fileName):
    f=open(fileName,"r",encoding="utf-8");
    global allDic
    for line in f.readlines():
        line=line.strip()
        if len(line)>1:
            allDic[line]=1
            
    f.close()
allDic={}
initNameDic('tbName.txt')
while 1:
    try:
        getDataOnce()
        time.sleep(15)
    except:
        print('fail')
        time.sleep(2)
