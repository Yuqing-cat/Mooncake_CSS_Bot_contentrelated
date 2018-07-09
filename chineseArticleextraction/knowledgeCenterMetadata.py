# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:45:38 2018

@author: yuqwe
"""

import os
import sys
# these is to import function from common folder
codePath = os.getcwd()
print("code Path is :\t", codePath)
os.chdir("..")
commonPath =  os.getcwd()+"\\common"
sys.path.append(commonPath)


import traverseFunction as x
import markdownParser as y
import csvReadWrite as z


def removeTag(contentList,ignoreTag,dictKey):
    print('before remove: ',len(contentList), 'lines of data')
    for tag in ignoreTag:
        i = 0
        while i < len(fileInfo):
            if fileInfo[i][dictKey] == tag:
                del fileInfo[i]
            else:
                i += 1
    print('after remove: ',len(fileInfo),'lines of data')

# extract useful key-value pair

def subDict(originDict, targetTag):
    destDict = []
    for f in originDict:
        x = {}
        for t in targetTag:
            if t in f.keys():
                x[t] = f[t]
            else:
                x[t] = 'NA'
                print(t,'is not in ', f['fileName'],' metadata')
        destDict.append(x)
    return destDict


dir = "D:\\GitHub\\acnContent\\"
# dir exist
x.dirExist(dir)

subFolder = ['az-docs-pr.zh-cn','mc-docs-pr.zh-cn']

dirPath = dir +subFolder[1] + "\\articles"

# set parameters
suffix = '.md'

# get all markdown files from selected folders
fileList, fileName, fileInfo = x.findSuffix(dirPath,suffix)


# ignore certain files 
ignoreTag = ['README','index']
removeTag(fileInfo,ignoreTag,'fileName')




### bug file: D:\\GitHub\\acnContent\\mc-docs-pr.zh-cn\\articles\\media-services\\media-services-deliver-streaming-content.md
#bugFile = "D:\\GitHub\\acnContent\\mc-docs-pr.zh-cn\\articles\\media-services\\media-services-deliver-streaming-content.md"
#index = 1488, only has one <hr>\n, re-write markdownParse get Header to solve
#a = y.getContent(fileInfo[1488])







# get real path
dir = "D:\\GitHub\\acnContent\\"
for file in fileInfo:
    file['realPath'] = file['fileLocation'].split(dir)[1]

# get content and extract header from content    
i = 0
fileMeta = []
for file in fileInfo: 
    print(fileInfo.index(file))
    y.getContent(file)
    
    split = '<hr>\n'
    print(i,file['fileName'],file['fileLocation'])
    i = i + 1
    # extract header info from content.
    if split in file['contents']:
        file = y.getHeader(file)
        fileMeta.append(file)
    else:
        print("not include header")
print(i,"file cotent extraction done.")
print(len(fileMeta),' files that have headers are stored into fileMeta.')




# choose certain tags
targetTag = ['fileName','title','description','ms.service','realPath','fileLocation']
articleMeta = subDict(fileMeta,targetTag)
print(len(articleMeta), 'files are extracted with target tags: \n',targetTag)

# generate url
preurl = 'https://docs.azure.cn/zh-cn/'
for file in articleMeta:
    #print(file['fileLocation'])
    #file['URL'] = x.getUrl(file['realPath'],preurl)
    file['URL'] = preurl + file['realPath'].split("\\")[-1].split(".")[0]

# store in csvs
'''
destPath = "D:\\GitHub\\Mooncake_CSS_Bot_contentrelated\\"
z.writeCsv(articleMeta,destPath+'kcMeta.csv')
print(len(articleMeta), "lines of knowledge center metadata is stored.")
'''




# store in csvs
destPath = "D:\\GitHub\\Mooncake_CSS_Bot_contentrelated\\chineseArticleextraction\\"
z.writeCsv(articleMeta,destPath+'kcMeta.csv')
print(len(articleMeta), "lines of aog metadata is stored.")

# clean for train classification
targetTag = ['title','description','ms.service']
kcCategory = subDict(fileMeta,targetTag)
print(len(kcCategory), 'files are extractedf with target tags: \n',targetTag)



destPath = "D:\\GitHub\\Mooncake_CSS_Bot_contentrelated\\chineseArticleextraction\\"
z.writeCsv(kcCategory,destPath+'kcCategory.csv')
