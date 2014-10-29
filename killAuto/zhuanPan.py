'''

'''
import re
import socket
import threading
import time
import urllib.parse
import urllib.request
import http.cookiejar
import json
from datetime import datetime


from fileNames import userFile, taskedUser, checkedProxyFile
from wwTools.fileTools import openFileToDic, dicRemove, getDicArr, openFileToArr,\
    appendData, hasFile
    
socket.setdefaulttimeout(10.0)

headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Host': 'www.ss911.cn',
    'Origin': 'http://www.ss911.cn',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection' : 'keep-alive',
    'Cookie' : 'lzstat_uv=27536272562782932456|264585; lzstat_ss=2912218113_0_1409145144_264585;ASP.NET_SessionId=sbskuxue4ljgl2552xvm5b55',
    #'Cookie' : 'RK=J5FrJKalWu; pt2gguin=o0484641127; ptcz=e9fe4398eb29335c4dd918e3326fc04dd2e294f2a7331a7abd6f39bd5faeee92; pgv_pvid=2092053654; o_cookie=484641127; uin=o484641127; skey=ZzqCm70ICM; itkn=1928745486',
    'Referer' : 'http://www.ss911.cn/Pages/login/login2.htm',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
    'X-Requested-With' : 'XMLHttpRequest'
            }
values = {
          'user' : 'shade372',
          'pass' : 'shade372',
          'code' : ''
         }

class IPGetter:

    def setProxy(self,proxy):
        socket.setdefaulttimeout(10.0)
        self.tProxy=proxy
        cj = http.cookiejar.CookieJar()
        proxy_handler = urllib.request.ProxyHandler({'http':self.tProxy})
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)

    def login(self):
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request("http://www.ss911.cn/Pages/login/login2.aspx",data,headers)
        self.opener.open(req)

    def getUIP(self):
        turl="http://t1.ss911.cn/Index.ss"
        req=urllib.request.Request(turl,None)
        pd=self.opener.open(req)
        dd=pd.read().decode('utf-8')
        self.getIPV(dd)

    def getIPV(self,txt):
        p=re.compile(r'fv.userip="(.*?)";')
        msp=p.search(txt)
        tip=msp.group(1)
        tip=urllib.parse.unquote(tip)
        sprint("ip:"+tip," "+self.tProxy)
        mylock.acquire()
        f=open("ipsn.txt","a",encoding="utf-8")
        f.write(tip+","+self.tProxy+"\n")
        f.close()
        mylock.release()


    def getUipByProxy(self,proxy):
        sprint('try:',proxy)
        self.setProxy(proxy)
        self.login()
        self.getUIP()
        mylock.acquire()
        f=open("goodProxyn4.txt","a",encoding="utf-8")
        f.write(proxy+"\n")
        f.close()
        mylock.release()

    def initTask(self):
        initV={"u":""}
        initV["u"]=self.user
        iUrl="http://t1.ss911.cn/Task/GetDayList.ss"
        data = urllib.parse.urlencode(initV)
        data = data.encode('utf-8')
        req = urllib.request.Request(iUrl,data)
        rst=self.opener.open(req).read().decode('utf-8')
        #print(rst)
    def setTask(self):
        initV={
            "u":"",
            "TaskID":"0"
            }
        initV["u"]=self.user
        iUrl="http://t1.ss911.cn/Task/SetDay.ss"
        data = urllib.parse.urlencode(initV)
        data = data.encode('utf-8')
        req = urllib.request.Request(iUrl,data)
        rst=self.opener.open(req).read().decode('utf-8')
        sprint(rst)
    def recoverZhuanPan(self):
        initV={"u":""}
        initV["u"]=self.user
        iUrl="http://t1.ss911.cn/Turn/RecoverTurn.ss"
        data = urllib.parse.urlencode(initV)
        data = data.encode('utf-8')
        req = urllib.request.Request(iUrl,data)
        rst=self.opener.open(req).read().decode('utf-8')
        rst=json.loads(rst)
        print(rst)
        
    def getZhuanPan(self):
        self.recoverZhuanPan()
        initV={"u":""}
        initV["u"]=self.user
        iUrl="http://t1.ss911.cn/Turn/CheckUser.ss"
        data = urllib.parse.urlencode(initV)
        data = data.encode('utf-8')
        req = urllib.request.Request(iUrl,data)
        rst=self.opener.open(req).read().decode('utf-8')
        rst=json.loads(rst)
        print(rst)
        #return
        if rst["nowFree"]>0:
            self.ZhuanPan()
        #{"endDay":3,"msg":"OK","nextTarget":"下一目标：积分达到1500 可以免费转7天 每天免费转1次","nowFree":1,"share":1,"totalFree":1}

    def ZhuanPan(self):
        initV={
            "u":"",
            "tCount":"1",
            "start":"0",
            "1":"0"
            }
        initV["u"]=self.user
        iUrl="http://t1.ss911.cn/Turn/TurnResult.ss"
        data = urllib.parse.urlencode(initV)
        data = data.encode('utf-8')
        req = urllib.request.Request(iUrl,data)
        rst=self.opener.open(req).read().decode('utf-8')
        rst=json.loads(rst)
        print(rst)
        #{'addGiftNum': 0, 'start': 0, 'objType': 0, 'result': 69, 'newVip': 0, 'turnID': 16139771, 'msg': 'OK', 'objID': 100167}
        #return
        if rst["turnID"]>0:
            appendData(self.user+","+str(rst["objID"])+"\n","outPuts/zhuanpan.txt")
            self.sendRst(rst["turnID"])
    def sendRst(self,tid):
        initV={
            "turnid":"",
            "tCount":"1",
            "start":"0",
            "1":"0"
            }
        initV["turnid"]=tid
        iUrl="http://t1.ss911.cn/Turn/SendGoods.ss"
        data = urllib.parse.urlencode(initV)
        data = data.encode('utf-8')
        req = urllib.request.Request(iUrl,data)
        rst=self.opener.open(req).read().decode('utf-8')
        rst=json.loads(rst)
        print(rst)
        
    def testWork(self):
        self.user="AYaj9+oHWbajAWD/kczujdtetcyOdOq+";
        self.setProxy("")
        self.getZhuanPan();
        
    def changeUser(self):
        self.user=getAUser()
    def workUser(self):
        self.changeUser()
        while 1:
            sprint('user:',self.user)
            if self.user==None:
                sprint("self.user==None:",self.user)
                return
            tProxy=getAProxy()
            #sprint('proxy:',tProxy)
            if tProxy==None:
                sprint("tProxy==None:",self.user)
                return
            else:
                self.setProxy(tProxy)
                try:
                    self.getZhuanPan()
                    sprint("success:"+self.user)
                    appendData(self.user+"\n",zhuanPanedUser())
                    self.changeUser()
                    time.sleep(1)
                except Exception as e:
                    sprint(e)
                    sprint("fail:",self.user)
                    time.sleep(1)





def getAUser():
    rst=None
    global userList
    mylock.acquire()
    if(len(userList)<1):
        pass
    else:
        rst=userList.pop()
    print('userLeft:',len(userList))
    mylock.release()


    return rst

def getAllUsers():
    f=open(userFile(),"r",encoding="utf-8")
    playerList=[]
    lines=f.readlines()
    f.close()
    for line in lines:
        line=line.strip().split(",").pop()
        if len(line)>1:
            playerList.append(line)


    print("user:",len(playerList))

    return playerList

def initUsers():
    global userList
    userList=[]
    allUserDic=getAllUsers()
    if hasFile(zhuanPanedUser()):
        taskedUserDic=openFileToDic(zhuanPanedUser())
    else:
        taskedUserDic={}

    toWorkUserDic=dicRemove(allUserDic,taskedUserDic)
    userList=getDicArr(toWorkUserDic)
    print("user:",len(userList))

    return userList

def getAProxy():
    rst=None
    global proxys
    mylock.acquire()
    if(len(proxys)<1):
        initProxy()
        rst=proxys.pop()
    else:
        rst=proxys.pop()
    mylock.release()
    return rst


def runAwork():
    getter=IPGetter()
    getter.workUser()



def sprint(*args):
    mylock.acquire()
    print(*args)

    mylock.release()
def initProxy():
    global proxys
    proxys=openFileToArr(checkedProxyFile())
    print('proxys:',len(proxys))
def beginWork():
    global mylock
    mylock=threading.Lock()
    global qcount
    qcount=0
    global proxys
    proxys=[]

    initUsers()
    initProxy()
    if len(proxys)<5000 and datetime.now().hour<8:
        print("proxy not enough wait next")
        return
    tCount=100;
    threads=[]
    for i in range(0,tCount):
        t=threading.Thread(target=runAwork)
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print('taskCheckEnd')


def testWork():
    getter=IPGetter()
    getter.testWork()
def workOnce():
    print("work")
    beginWork()

def work():
    cdTime=60*60*1
    while 1:
        try:
            workOnce()
            time.sleep(cdTime)
        except Exception as e:
            print(e)
            time.sleep(cdTime)
            
if __name__ == '__main__':
    #workOnce()
    work()
    #testWork()
    pass
