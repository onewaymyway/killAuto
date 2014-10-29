from wwTools.fileTools import getDateName


def rawProxyFile():
    return "rawProxy/"+getDateName()+".txt"

def checkedProxyFile():
    return "checkedProxy/"+getDateName()+".txt"

def regedProxy():
    return "regedProxy/"+getDateName()+".txt"

def taskedUser():
    return "taskedUser/"+getDateName()+".txt"

def zhuanPanedUser():
    return "zhuanPanedUser/"+getDateName()+".txt"

def userFile():
    return "regUser/rgd.txt"

if __name__ == '__main__':
    pass
