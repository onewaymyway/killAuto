import os
from PIL import Image

threshold = 70
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(255)

outpath='out'

tRstStr=''
def checkPic(pic):
    cmd='tesseract '+pic+' '+outpath+' -psm 7'
    #os.system(cmd)
    os.popen(cmd).readlines()

def showRst():
    f=open(outpath+'.txt','r',encoding='utf8')
    rst=f.readline()
    rst=rst.replace(' ','')
    ft=filter(str.isalnum,rst)
    rst=''
    for kk in ft:
        rst+=kk
    f.close()
    print(rst)
    return rst


def convertPic(pic):
    im=Image.open(pic);
    ims=im.convert('L')
    out=ims.point(table,'L')
    out.save('tem.jpg') 
    return out

def checkAndSave(pic):
    op=convertPic(pic)
    checkPic('tem.jpg');
    rst=showRst();
    return rst
    op.save('rst/'+rst+'.jpg')

def simpleTest():
    for id in range(1,30):
        checkAndSave('yzma'+str(id)+'.png')
    
    
if __name__=='__main__':
    print('hello yzm')
    checkAndSave('yzma.png')
else:
    pass

    

