# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:36:16 2018

@author: yuqwe
"""

import xml.etree.cElementTree as ET
import xmlFunction as x 
import csv


# get external url, file location, productname 
dir = "C:\\acn-portal-pr.zh-cn\\marketing-resource\\xml\\home\\features"
preurl = 'https://www.azure.cn/zh-cn/'
urlList, fileList, products = x.getXmlLocation(dir,preurl)


tags = ['bodyText']


def getXmlText(child,tags):
    metaDict = {}
    childTags = []
    texts = []
    for i in tags: 
        for sub in child.iter(tag=i):
            childTags.append(sub.tag)
            texts.append(sub.text)
            metaDict[sub.tag] = sub.text           
            #result = sub.tag,':',sub.text
            #results.append(result)
            #print(sub.tag,':',sub.text)
    #print(metaDict)
    return metaDict



count = 0
contents = []
file= fileList[0]
    #print(file)
xmlTree = ET.parse(file)
xmlRoot = xmlTree.getroot()

count = count+1
#print(count)
for child in xmlRoot:
    content = getXmlText(child,tags)
    for sub in child.iter(tag='bodyText'):
        content2 = getXmlText(sub,tags)
        print("###################\n",sub.tag)
        print("###################\n",sub.text)
        m = sub.text
contents.append(content)
#print('There are {} articles in this list, {} of them has {} content is as followed:'.format(count,len(contents),tags))
#print(contents)


import re 

n = re.findall(r'(?<=<p>).+?(?=</p>)|(?<=<h2>).+?(?=</h2>)|(?<=<h3>).+?(?=</h3>)',m)
n