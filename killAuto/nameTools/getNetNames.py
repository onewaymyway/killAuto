import re
import urllib.parse
import urllib.request
import http.cookiejar

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
    req=urllib.request.Request(url,None,headers)
    cdata=opener.open(req).read()
    #print(cdata)
    data=cdata.decode('utf-8')
    return data
def getProxyList(pTxt):
    #pre=re.compile(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>whois</td><td><div class="addr_style">(.*?)</div></td></tr>')
    pre=re.compile(r'<li><p>(.*?)</p></li>')
    #print(pTxt)

    matches=pre.findall(pTxt)
    #print(matches)
    global proxyList
    for tP in matches:
        #print(tP)
        tip=tP;
        if len(tip)<=7:
            proxyList.append(tip)
        
        print(tip)

def getProxyByUrl(url):
    print('tryget:'+url)
##    ptxt=getProxyHttp(url)
##    getProxyList(ptxt)
##    return
    try:
        ptxt=getProxyHttp(url)
        getProxyList(ptxt)
    except:
        print("fail:"+url)
    
def saveProxyFile(pList):
    f=open("netNameListchaozhuai.txt","w",encoding="utf-8");
    data="\n".join(pList)
    txt=f.write(data);
    f.close()

#getProxyByUrl('http://www.oicq88.com/feizhuliu/15.htm')

for i in range(1,37):
    getProxyByUrl('http://www.oicq88.com/chaozhuai/'+str(i)+'.htm')
saveProxyFile(proxyList)
