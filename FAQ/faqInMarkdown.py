# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:54:06 2018

@author: yuqwe
"""

import os

dir = "C:\\Users\\yuqwe\\Documents\\GitHub\\az-docs-pr.zh-cn\\"



# dir exist
if os.path.exists(dir):
    print("{} dir exists.".format(dir))
else:
    print("{} dir not found.".format(dir))


# is file or folder
if os.path.isfile(dir):
    print("{} is a file.".format(dir))
else:
    print("{} is not a file or not found.".format(dir))

# get file size
fileSize = os.path.getsize(dir)

# parameters
fileList = []
suffix = '.md'

# traverse folder
for (root,dirs,files) in os.walk(dir):
    n = 0
    m = 0
    print(files)
    for filename in files:
        if os.path.splitext(filename)[1] == suffix:
            fileList.append(os.path.join(root,filename))
            n = n + 1
            print(n)
            #print(filename)

        m = m + 1
    if n > 0:
        print("there are {} out of {} files have suffix {}.".format(n,m,suffix))



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
