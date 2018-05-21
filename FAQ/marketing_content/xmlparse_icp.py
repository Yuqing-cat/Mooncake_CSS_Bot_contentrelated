# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:44:37 2018

@author: yuqwe
"""

import xmlFunction as x 
import csv

###the following is for support
# get external url, file location, productname 
dir = "D:\\acn-portal-pr.zh-cn\\marketing-resource\\xml\\icp"
preurl = 'https://www.azure.cn/zh-cn/'
urlList, fileList, products = x.getXmlLocation(dir,preurl)
# product is useless here, need to generate filename with url

# add icp.xml into this category
urlList.append("https://www.azure.cn/zh-cn/icp/")
fileList.append("D:\\acn-portal-pr.zh-cn\\marketing-resource\\xml\\icp.xml")



#tags = ['metaDescription']
tags = ['pageTitle','linkid','metaKeywords','metaDescription','urlDisplayName','bodyText']
content = x.getXmlContent(fileList,tags)

# add 
n  = 0
for i in content:
    i['URL'] = urlList[n]
    i['fileCategory'] = 'icp'
    i['metaDescription'] = str(i['metaDescription']).replace("\n","")
    i['metaDescription'] = str(i['metaDescription']).replace(" ","")
    n = n+1
    print(i['metaDescription'])


# parse p ~ h4 from boty text
import re
n = 0
for i in content:
    m = i['bodyText']
    x = re.findall(r'(?<=<p>).+?(?=</p>)|(?<=<h2>).+?(?=</h2>)|(?<=<h3>).+?(?=</h3>)|(?<=<h4>).+?(?=</h4>)',m)
    i['bodyText'] = x
    print(x)
    
# write into product csv
i = 0
for p in urlList:
    p = str(p).replace("https://www.azure.cn/zh-cn/","")
    p = str(p).replace("/","-")
    file = p[:-1]+'.csv'
    print(file)
    with open(file,'w',newline='',encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(content[i].keys())
        w.writerow(content[i].values())
    i = i+1
    print(i)