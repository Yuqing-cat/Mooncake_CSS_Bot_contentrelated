# this file extract marketing content from /home/features folder
import xmlFunction as x 
import csv


# get external url, file location, productname 
dir = "C:\\acn-portal-pr.zh-cn\\marketing-resource\\xml\\home\\features"
preurl = 'https://www.azure.cn/zh-cn/'
urlList, fileList, products = x.getXmlLocation(dir,preurl)

# get content 
tags = ['pageTitle','linkid','metaKeywords','mataDescription','urlDisplayName','bodyText']

#tags = ['metaDescription']
content = x.getXmlContent(fileList,tags)




n  = 0
for i in content:
    i['URL'] = urlList[n]
    i['fileCategory'] = 'features'
    n = n+1
    print(i)


import re
n = 0
for i in content:
    m = i['bodyText']
    x = re.findall(r'(?<=<p>).+?(?=</p>)|(?<=<h2>).+?(?=</h2>)|(?<=<h3>).+?(?=</h3>)|(?<=<h4>).+?(?=</h4>)',m)
    i['bodyText'] = x
    print(x)


# json
import json
i = 0
for p in products:
    file = p+'.json'
    print(file)
    with open(file,'w',newline='',encoding='utf-8-sig') as f:
        print(content[i])
        n=json.dump(content[i],f,ensure_ascii=False,indent=4)
        print(n)
        print(i)
    i = i+1



# csv 
i = 0
for p in products:
    file = p+'.csv'
    print(file)
    with open(file,'w',newline='',encoding='utf-8-sig') as f:
        w = csv.writer(f)
        #w.writerow(content[])
        #for key,val in content[i].items():
         
        #print(key,val)
        #   w.writerow([key,val])
    i = i+1


i = 0
for p in products:
    file = p+'.csv'
    print(file)
    with open(file,'w',newline='',encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(content[1].keys())
        w.writerow(content[1].values())
    i = i+1
print(i)

'''
# print out product list

count = len(products)
for i in 0:
    print(product)

  
print(urlList)
print(fileList)


# parse xml files in the file location list


xmlTree = ET.parse(fileList[0])
xmlRoot = xmlTree.getroot()
#print('root-tag:',xmlRoot.tag,',root-attrib:',xmlRoot.attrib,',root-text:',xmlRoot.text)

count = 1
contents = []
for file in fileList:
    #print(file)
    xmlTree = ET.parse(file)
    xmlRoot = xmlTree.getroot()
    tags = ['pageTitle','linkid','metaKeywords','mataDescription','urlDisplayName']
    print(count)
    count = count+1
    for child in xmlRoot:
        content = xmlFunction.getXmlText(child,tags)
    contents.append(content)
print('there are {} articles in this folder: {}, and the content is as followed:'.format(count,dir))
print(contents)
                
'''
