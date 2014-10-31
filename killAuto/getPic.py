
import urllib.request
from fileNames import userFile, taskedUser, checkedProxyFile
from wwTools.fileTools import openFileToDic, dicRemove, getDicArr, openFileToArr,\
    appendData, hasFile,saveData,getDicStr,getArrStr

def getPic(id):
    urllib.request.urlretrieve("http://t1.ss911.cn/resource/tool/%s.png"%id,'rsts/pics/%s.jpg'%id)

def getArr(fileName):
    f=open(fileName,"r",encoding="utf-8");
    rst=[]
    goodList=[]
    dic={}
    playerDic=getAllUsers()
    for line in f.readlines():
        line=line.strip()
        arr=line.split(",")
        tGood=arr[1]
        tUser=playerDic[arr[0]]
        if tGood in dic:
            dic[tGood]+=1
        else:
            dic[tGood]=1
        if tGood in rst:
            pass
        else:
            rst.append(tGood)
        if int(tGood)<100000:
            goodList.append(tUser+":"+tGood)
        
    f.close()
    return rst,dic,goodList

def writeCount(dic):
    rst=[];
    for kk in dic:
        rst.append(str(kk)+":"+str(dic[kk]))
    f=open("rsts/count.txt","w",encoding="utf-8");
    f.write("\n".join(rst))
    f.close()

def getAllUsers():
    f=open(userFile(),"r",encoding="utf-8")
    playerList={}
    lines=f.readlines()
    f.close()
    for line in lines:
        line=line.strip()
        token=line.split(",").pop()
        if len(token)>1:
            playerList[token]=line

    return playerList
    
def getPics(fileName):
    arr,dic,goodList=getArr(fileName)
    writeCount(dic)
    saveData(getArrStr(goodList),"rsts/userGood.txt")
    return
    for id in arr:
        try:
            getPic(id)
            print("ok")
        except:
            print("fail:",id)

#getPics("zhuanpanRst.txt")
getPics("outPuts/zhuanpan.txt")
print("ok")

    
