
import urllib.request

def getPic(id):
    urllib.request.urlretrieve("http://t1.ss911.cn/resource/tool/%s.png"%id,'pics/%s.jpg'%id)

def getArr(fileName):
    f=open(fileName,"r",encoding="utf-8");
    rst=[]
    dic={}
    for line in f.readlines():
        line=line.strip()
        arr=line.split(",")
        if arr[1] in dic:
            dic[arr[1]]+=1
        else:
            dic[arr[1]]=1
        if arr[1] in rst:
            pass
        else:
            rst.append(arr[1])
        
    f.close()
    return rst,dic

def writeCount(dic):
    rst=[];
    for kk in dic:
        rst.append(str(kk)+":"+str(dic[kk]))
    f=open("count.txt","w",encoding="utf-8");
    f.write("\n".join(rst))
    f.close()
    
def getPics(fileName):
    arr,dic=getArr(fileName)
    writeCount(dic)
    return
    for id in arr:
        try:
            getPic(id)
            print("ok")
        except:
            print("fail:",id)

#getPics("zhuanpanRst.txt")
getPics("../outPuts/zhuanpan.txt")

    
