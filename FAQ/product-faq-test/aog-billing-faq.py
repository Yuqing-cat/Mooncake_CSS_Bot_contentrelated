# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:39:21 2018

@author: yuqwe
"""

import sys
import traverseFunction as x
import markdownParser as y 
import csv
import re

dir = "C:\\Users\\yuqwe\\Documents\\GitHub\\az-docs-pr.zh-cn\\others\\azure-operations-guide\\commerce\\billing\\"



x.dirExist(dir)
suffix = '.md'

# get all markdown files from selected folders
fileList, fileName, fileInfo = x.findSuffix(dir,suffix)

# generate url
preurl = 'https://docs.azure.cn/zh-cn/'
for file in fileInfo:
    print(file['fileLocation'])
    file['URL'] = x.getUrl(file['fileLocation'],preurl)


# extract markdown content.
i = 0
for file in fileInfo: 
    y.getContent(file)
    split = '<hr>\n'
    #print(i,file['fileName'],file['fileLocation'])
    i = i + 1
    # extract header info from content.
    if split in file['contents']:
        file = y.getHeader(file)
    else:
        print("not include header")
print(i,"file cotent extraction done.")

# search faq related files 
text = ['常见问题','faq','FAQ']
textIndex = y.searchText(fileInfo,text)

for i in textIndex:
    print(i)
    print('\t文章标题：\t',fileInfo[i]['title'])
    print('\t文件名\t',fileInfo[i]['fileName'])
    print('\t路径\t',fileInfo[i]['fileLocation'])
    print('\t链接\t',fileInfo[i]['URL'])
    #print('\t内容\t',fileInfo[i]['bodyContent'])
    question = []
    n = 0
    for m in fileInfo[i]['bodyContent']:
        question = re.findall(r'(?<=<h2>).+?(?=</h2>)',m)
        if question is not []:
            question.append
        print('\t\t',questions)
    


