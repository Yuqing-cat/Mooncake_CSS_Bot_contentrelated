# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:58:52 2018

@author: yuqwe
"""

import os 


def dirExist(dir):
    if os.path.exists(dir):
        print("{} \ndir exists.".format(dir))
    else:
        print("{} \ndir not found.".format(dir))


def dirIsFile(dir):
    if os.path.isfile(dir):
        print("{} is a file.".format(dir))
    else:
        print("{} is not a file or not found.".format(dir))
    

def findSuffix(dir, suffix='.md'):
    fileCount = []
    suffixCount = []
    fileInfo = []
    fileList = []
    fileName= []
    
    # traverse folder
    
    for (root,dirs,files) in os.walk(dir):
        fileCount.append(len(files))
        n = 0
        #print(files)
        for filename in files:
            if os.path.splitext(filename)[1] == suffix:
                filelocation = os.path.join(root,filename)
                fileList.append(filelocation)
                n = n + 1
                name = str(filename).replace(".md","")
                fileName.append(name)
                fileInfo.append({'fileLocation':filelocation,'fileName':name})
        suffixCount.append(n)
    '''
        if n > 0:
            print("there are {} out of {} files with suffix {}.\n".format(n,len(files),suffix))
    '''
    print("There are totoal {} files in dir: {}.".format(sum(fileCount),dir))
    print("Among them, {} of these files are {} files \nTheir location stored in fileList.\nTheir file name stored in fileName".format(sum(suffixCount),suffix))
    #print("the fileList is:",fileList,"\n")
    #print("the fileName is:",fileName,"\n")
    return fileList, fileName,fileInfo

def getUrl(realPath,preurl = 'https://docs.azure.cn/zh-cn/'):
    url_temp = realPath.split("\\")
    #print("split file location: ",url_temp)
    url_temp[-1] = (url_temp[-1].split("."))[0]
    #print("remove file type: ",url_temp)
    del url_temp[0]
    #print("remove location dir",url_temp)
    if url_temp[0] == 'others':
        url_temp[0] = 'articles'
    endurl = "/".join(url_temp)
    #print(endurl)
    url = preurl + endurl + '/'
    print("url\t",url,"filePath\t",realPath)
    return url

    