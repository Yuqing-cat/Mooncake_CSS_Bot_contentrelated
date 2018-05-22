# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:54:06 2018

@author: yuqwe
"""
import sys
import mistune
import traverseFunction as x
import re

dir = "C:\\Users\\yuqwe\\Documents\\GitHub\\az-docs-pr.zh-cn\\"

# dir exist
x.dirExist(dir)

# set parameters
suffix = '.md'

fileList, fileName, fileInfo = x.findSuffix(dir,suffix)


for file in fileInfo: 
    filename = file['fileName']
    print(file)
    location = file['fileLocation']
    with open(location, encoding='utf-8',mode='r') as f:
        contents = []
        for line in f:
            contents.append(repr(line))
            print(repr(line))
        file['contents'] = contents
    #html = mistune.markdown(

    
for file in fileInfo:    
    filename = file['fileName']
    if "faq" in filename:
        print(file['fileLocation'])
    #html = mistune.markdown(



############## test in specific file     
# extract markdown content 
    file = fileInfo[19]
    filename = file['fileName']
    #print(file)
    location = file['fileLocation']
    with open(location, encoding='utf-8',mode='r') as f:
        contents = []
        detail = {}
        i = 0
        for line in f:
            i = i + 1
            content = mistune.markdown(line, escape = True)
            print(i,":",content)
            contents.append(content)
    file['contents'] = contents
    #print(file)

# fine <hr> in content
    a = file['contents']
    enumerate(a)
    headIndex = [i for i, x in enumerate(a) if x == "<hr>\n"]
    startIndex = headIndex[0]+1
    endIndex = headIndex[1]
    headContent = a[startIndex:endIndex]
    print(headContent)
    for i in headContent:
        x = re.findall(r'(?<=<p>).+?(?=</p>)',i)
        x = x[0].split(":")
        key = x[0]
        value = x[1]
        file[key] = value
        print(x)
    print('title: ',file['title'])   
    print('description: ',file['description'])  
    print(file['fileLocation'])
    
    
        
    
        

import re
n = 0
for i in content:
    m = i['bodyText']
    x = re.findall(r'(?<=<p>).+?(?=</p>)|(?<=<h2>).+?(?=</h2>)|(?<=<h3>).+?(?=</h3>)|(?<=<h4>).+?(?=</h4>)',m)
    i['bodyText'] = x
    print(x)












'''

    
    
    file = fileInfo[100]
    filename = file['fileName']
    #print(file)
    location = file['fileLocation']
    with open(location, encoding='utf-8',mode='r') as f:
        contents = []
        detail = {}
        i = 0
        for line in f:
            i = i + 1
            print(i,":",mistune.markdown(line, escape = True))
            if "title:" in line:
                detail['title'] = line
            if "[中文]:" in line:
                detail['chineseUrl'] = line
            if "[英文]：" in line:
                detail['englishUrl'] = line
            if "description:" in line:
                detail['description'] = line
            if "keywords:" in line:
                detail['keywords'] = line
            if "ms.service:" in line:
                detail['ms.service'] = line   
                
            #print(mistune.markdown(line, escape = True))
        print(detail)

            
            
            contents.append(repr(line))
            print(repr(line))
        file['contents'] = contents
'''