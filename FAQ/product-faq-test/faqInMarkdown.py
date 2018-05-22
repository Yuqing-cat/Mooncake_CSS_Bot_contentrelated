# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:54:06 2018

@author: yuqwe
"""

import os
import traverseFunction as x

dir = "C:\\Users\\yuqwe\\Documents\\GitHub\\az-docs-pr.zh-cn\\"

# dir exist
x.dirExist(dir)

# set parameters

fileCount = []
suffix = '.md'
suffixCount = []
fileList = []
fileName= []

# traverse folder

for (root,dirs,files) in os.walk(dir):
    fileCount.append(len(files))
    n = 0
    #print(files)
    for filename in files:
        if os.path.splitext(filename)[1] == suffix:
            fileList.append(os.path.join(root,filename))
            n = n + 1
            name = str(filename).replace(".md","")
            fileName.append(name)
    suffixCount.append(n)
'''
    if n > 0:
        print("there are {} out of {} files with suffix {}.\n".format(n,len(files),suffix))
'''
print("There are totoal {} files in dir: {}.".format(sum(fileCount),dir))
print("Among them, {} of these files are {} files \nTheir location stored in fileList.\nTheir file name stored in fileName".format(sum(suffixCount),suffix))
#print("the fileList is:",fileList,"\n")
#print("the fileName is:",fileName,"\n")



def isSuffix(path, suffix):
    fileList = os.listdir(path)
    n = 0
    m = 0
    suffixList = []
    for file in fileList:
        if os.path.splitext(file)[1] == suffix:
            n = n+1
            suffixList.append(file)
        m = m+1
    print("there are {} out of {} files have suffix {}.".format(n,m,suffix))
    return suffixList


isSuffix(dir,'.md')
