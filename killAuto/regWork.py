#! /usr/bin/env python3
#coding=utf-8
import urllib.parse
import urllib.request
import json
import time
import socket
import http.cookiejar
import random
import re
from yzm import checkYZM
from wwTools.fileTools import openFilesToArr, arrAdd, arrRemove, appendData,\
    openFileToArr, hasFile
from fileNames import checkedProxyFile, regedProxy, userFile
#from bs4 import BeautifulSoup

#url = 'http://api.open.baidu.com/pae/channel/data/asyncqury?cb=jQuery110209612188022583723_1405057078072&appid=4001&com=shentong&nu=768936885065&_=1405057078095'
url = 'http://api.open.baidu.com/pae/channel/data/asyncqury'
url="http://www.ss911.cn/pages/reg/regUser.aspx";

socket.setdefaulttimeout(8.0)

tNum=50003251804803;

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#district=0&hcountry=0&hprovince=0&hcity=0&hdistrict=0&online=1&ldw=360759066
values = {
          #'cb' : 'jQuery110209612188022583723_1405057078072',
          '__EVENTTARGET' : '',
          '__EVENTARGUMENT' : '',
          '__VIEWSTATEGENERATOR':'BAE963F9',
          '__VIEWSTATE' : '/wEPDwUJMTI5NzM2MzEyZGQtK89ZN0vZ8S3X+JMEdRXK0D+GdA==',
          '__EVENTVALIDATION' : '/wEWBwLjoKOoCgLEhISACwLKw/ZKAsrDurkGAoTz/f8JApL76rYEAoznisYGiFIqlKd3My1jS4ZtTKrb9MFd9us=',
          'txtname' : 'kill011',
          'txtpass1' : 'deathnote123',
          'txtpass2' : 'deathnote123',
          'txtemail' : 'guiyank@126.com',
          'txtyzm' : 'ucva',
          'Button1' : '提交注册'
         }

values['nu']=tNum;
qqID="595912947";

headers = {
    'Accept' : 'application/json',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Host': 'www.ss911.cn',
    'Origin': 'http://www.ss911.cn',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection' : 'keep-alive',
    'Cookie' : 'lzstat_uv=27536272562782932456|264585; lzstat_ss=2912218113_0_1409145144_264585;ASP.NET_SessionId=sbskuxue4ljgl2552xvm5b55',
    #'Cookie' : 'RK=J5FrJKalWu; pt2gguin=o0484641127; ptcz=e9fe4398eb29335c4dd918e3326fc04dd2e294f2a7331a7abd6f39bd5faeee92; pgv_pvid=2092053654; o_cookie=484641127; uin=o484641127; skey=ZzqCm70ICM; itkn=1928745486',
    'Referer' : 'http://www.ss911.cn/pages/reg/regUser.aspx',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
    'X-Requested-With' : 'XMLHttpRequest'
            }


#tProxy="117.21.192.10:80"
#tProxy="127.0.0.1:8080"
iprecord=0
displayed={};
ISOTIMEFORMAT='%Y-%m-%d %X'
hidenget=0

def getAProxy():
    
    newProxy=openFileToArr(checkedProxyFile())
    global proxys
    
    tregedProxy=openFileToArr(regedProxy())
    
    proxys=arrRemove(newProxy,tregedProxy)
    
    if len(proxys)<1:
        return None
    rst=proxys.pop()
    print('setProxy:'+rst)
    
    appendData(rst+"\n",regedProxy())

    return rst


    
def changeIP():
    global hidenget
    hidenget=0
    global texpt
    texpt=0
    global tProxy
    tProxy=getAProxy()
    #tProxy="127.0.0.1:8080"
    
    if tProxy==None:
        print("no proxy available,wait")
        time.sleep(60)
        return
    
    global iprecord
    iprecord=0
    global cj
    cj = http.cookiejar.CookieJar()
    proxy_handler = urllib.request.ProxyHandler({'http':tProxy})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    global opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)

def getWeb():
    url='http://www.ss911.cn/pages/reg/regUser.aspx'
    req=urllib.request.Request(url)
    global opener
    response=opener.open(req)
    data=response.read().decode('utf-8')
    #print(data)
    return data

def getValues(txt):
    p=re.compile(r'input type="hidden" name="(.*?)" id="(.*?)" value="(.*?)" ')
    msp=p.findall(txt)
    global values
    #data={}
    for kk in msp:
        #print(kk)
        key=kk[0]
        value=kk[2]
        values[key]=value

    #print(data)
    
def getHidden():
    print('try get Hidden')
    txt=getWeb()
    getValues(txt)
    global hidenget
    hidenget=1
    
def regCount():
    uname=getARandomEName()
    global hidenget
    if hidenget<1:
        getHidden()
    getYzm()
    time.sleep(1)
    print('keyword:',uname)
    values["txtname"]=uname;
    print('uname:',uname,'-')
    values["txtemail"]=uname+"@126.com";
    values["txtpass1"]=uname;
    values["txtpass2"]=values["txtpass1"]
    #yzm = input('Enter yzm: ')
    yzm=checkYZM.checkAndSave('yzma.png')
    
    print(yzm)
    
    values["txtyzm"]=yzm
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    turl=url;
    req = urllib.request.Request(turl,data,headers)
    #response = urllib.request.urlopen(req)
    response = opener.open(req)
    the_page = response.read()
    rstTxt=the_page.decode('utf-8')
    
    print(cj)
    if rstTxt.find('常见问题解答')>=0:
        for cks in cj:
                print(cks.name+" "+urllib.parse.unquote(cks.value))
                if(cks.name=="uservalues"):
                  tUserValue=urllib.parse.unquote(cks.value)
        print('注册成功')
        print(uname," ",tUserValue)
        dname=setName(tUserValue)
        f=open(userFile(),"a",encoding="utf-8")
        rst=[uname,values["txtpass1"],values["txtemail"],dname,tUserValue]
        str=','.join(rst)
        f.write(str+"\n")
        f.close()
        getUIP()
    elif rstTxt.find('IP超过了注册上限，不能注册！')>=0:
        print('IP超过了注册上限')
        changeIP()
    elif rstTxt.find('该用户名已经被注册了')>=0:
        print('该用户名已经被注册了')
    elif rstTxt.find('验证码输入不正确！')>=0:
        print('验证码输入不正确！')
    
    else:
        print(rstTxt)
        print('注册失败')
    #regCount()



def getYzm():
    print('try get Yzm')
    value={"dt":"Wed Aug 27 2014 16:33:02 GMT 0800 (中国标准时间)"}
    value['qt']=time.ctime()+' GMT 0800 (中国标准时间)'
    purl="http://www.ss911.cn/pages/yzm.aspx?"+urllib.parse.urlencode(value)
    req=urllib.request.Request(purl,None,headers)

    #urllib.request.urlretrieve(req,"yzm.jpg")
    pd=opener.open(req)
    pic=pd.read()
    f=open("yzma.png","wb")
    f.write(pic);
    f.close()


def setName(uvalue):
    tname=getARandomName()
    print('trySetName:',tname,'-')
    nameValue={
        "username":tname,
        "sex":getArandomSex(),
        "uv":uvalue,
        "rd":""
        }
    nameValue['rd']=9999*random.random()
    nameValue['rd']='8468.362554495223'
    tnameUrl="http://t1.ss911.cn/User/Register.ss?"+urllib.parse.urlencode(nameValue)
    req=urllib.request.Request(tnameUrl,None)
    pd=opener.open(req)
    dd=pd.read().decode('utf-8')
    print(dd)
    if dd.find('OK')>=0:
        print('改名成功')
        return tname
    else:
        print('名字重复，尝试新名字')
        time.sleep(1)
        return setName(uvalue)

def getUIP():
    turl="http://t1.ss911.cn/Index.ss"
    req=urllib.request.Request(turl,None)
    pd=opener.open(req)
    dd=pd.read().decode('utf-8')
    getIPV(dd)

    
def getNewName(oname):
    return oname+"s"

def initNamedic():
    namefiles=[
        'tbName'
        ]
    for filename in namefiles:
        addNameDic('nameTools/'+filename+'.txt')

def addNameDic(fileName):
    global namedic
    tlist=openFileToArr(fileName)
    namedic=arrAdd(namedic,tlist)
    print('len:',len(namedic))

def getARandomName():
    tlen=len(namedic)
    tc=int(tlen*random.random())%tlen
    return namedic[tc]

def getArandomSex():
    if random.random()>0.4:
        return "0"
    else:
        return "1"

def preDealE():
    f=open("enames.txt","r",encoding="utf-8")
    wf=open("enamess.txt","w",encoding="utf-8")
    ck=[]
    for line in f.readlines():
        if line.find('.')<0:
            ck.append(''.join(line.split()))
    wf.write(",".join(ck));
    f.close();
    wf.close();
def initEnames():
    f=open("nameTools/enamess.txt","r",encoding="utf-8");
    namets=f.readline();
    global enamedic
    enamedic=namets.split(',')
    print('len:',len(enamedic))
    f.close()

def getARandomEName():
    tlen=len(enamedic)
    tc=int(tlen*random.random())%tlen
    ti=str(int(999*random.random()))
    rst=enamedic[tc]+ti
    if len(rst)>12:
        rst=rst[0:11]
    return rst

def getIPV(txt):
    global iprecord
    if iprecord>0:
        return
    iprecord=1
    p=re.compile(r'fv.userip="(.*?)";')
    msp=p.search(txt)
    tip=msp.group(1)
    tip=urllib.parse.unquote(tip)
    print("ip:"+tip," "+tProxy)
    f=open("outPuts/ips.txt","a",encoding="utf-8")
    f.write(tip+","+tProxy+"\n")
    f.close()
 
 
def work():
    initNamedic();
    print(getARandomName())
    initEnames();
    print(getARandomEName())
    texpt=0
    global tWorkCount
    changeIP()
    while(1):
        tWorkCount=tWorkCount+1
        if tWorkCount>200:
            tWorkCount=1
            initNamedic()
        try:
            regCount()
        
        except Exception as e:
            print(e)
            texpt=texpt+1
            if(texpt>3):
                texpt=0
                changeIP()
namedic=[];
enamedic=[];
proxys=[]
tsname="potaa"
tWorkCount=1
#regCount()
if __name__ == '__main__':
    work()
    pass
