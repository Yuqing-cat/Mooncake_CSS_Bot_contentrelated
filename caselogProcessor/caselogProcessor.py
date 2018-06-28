# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:44:06 2018

@author: yuqwe
"""

import csv
import re
#FUNCTIONS

# trasnform csv into dictionary
def csvToDict(fileLocation, headers,header =True):
    rows = []
    dicts = []
    with open(fileLocation,'r',newline="", encoding = "utf-8") as f:
            reader = csv.reader(f)
            if header == True:
                # to skip header
                next(reader,None)
                print("header is ignored.")
            else:
                print("the csv file is set as no-header.")
            csv_dict = {}
            i = 0
            for row in reader:
                csv_dict = {headers[0]:row[0],headers[1]:row[1]}
                #print(row[1])
                rows.append(row)
                dicts.append(csv_dict)
                i = i+ 1
            print(i, ' rows of data in loaded into python')
            return dicts

def dictStringRemove(originDict,key,removeString):
    for i in removeString:
        originDict[key] = originDict[key].replace(i,'')
    #print(originDict)
    print("the content is cleaned by dictStringRemove.")
    return originDict


# deduplicate content
def dedupContent(contentDict):
    dupContentDict = []
    dupContentTitle = []
    dedupContentDict = []
    dedupContentTitle = []
    for i in contentDict:
        if i['case.title'] in dedupContentTitle:
            dupContentDict.append(i)
            dupContentTitle.append(i['case.title'])
        else:
            dedupContentDict.append(i)
            dedupContentTitle.append(i['case.title'])
    print(len(dedupContentDict)," line of distinct caselog is filtered out.")
    print(len(dupContentTitle), " line of caselog is same, please lookinto them. these should be faq!")
    #print("\t",dupContentTitle)    
    return dupContentDict,dedupContentDict


# print list line by line
def printList(list):
    lineNumber = 0
    for i in list:
        lineNumber += 1
        print(lineNumber,'\t',i)
    print("the list ends.")
    print("it contains ", lineNumber, " lines in total.")

# write list of dicts into csv
def writeCsv(sourceList, destFile):
    with open(destFile,'w',newline='',encoding = 'utf-8') as f:
        w = csv.writer(f)
        w.writerow(sourceList[0].keys())
        for i in sourceList:
            w.writerow(i.values())
# MAIN
            
# set file location
dir = "C:\\Users\\yuqwe\\Source\\Repos\\Mooncake CSS ChatBot\\data\\caselog\\"
caselogTag = dir+'caselogTag.csv'
caselogRaw = dir+'caselogRaw.csv'


# load tags from csv
tagDict = csvToDict(caselogTag,['case.productName','ms.service'], True)

# load content from csv
contentDict = csvToDict(caselogRaw,['case.title','case.productName'],True)

# extract removeString like '[HMC]' tags from case.title
removeString = set()
for i in contentDict:
    rawString= re.findall('[[](.*?)[]]',i['case.title'])
    for s in rawString:
        s = '['+s+']'
        #print(s)
        removeString.add(s) 
print("the following tags will be removed",removeString)



# if the removeString is not suitable, we can force it as followed
#removeString = ['[MS-LED]','[PIA]','[HMC]','[ms-led]','[EA Trial]']
# replace content
contentCount = 0
for i in contentDict:
    i = dictStringRemove(i,'case.title',removeString)
    contentCount += 1
print(contentCount, " lines of caselog in cleaned and stored in contentDic.")


# deduplicate content and store those faq into caselogFaqDict
caselogFaqDict, dedupContentDict = dedupContent(contentDict)

# join caselog content with tag
tagq = []
untagq = []
for i in dedupContentDict:
    tagCount = len(tagDict)
    for tag in tagDict:
        if i['case.productName'] ==tag['case.productName']:
            i['ms.service'] = tag['ms.service']
            tagq.append(i)
            break
        else:
            tagCount -= 1
    if tagCount == 0:
        untagq.append(i)
print(len(tagq)," lines of caselog has ms.service tag")
print(len(untagq)," lines of caselog doesn't have ms.service tag")


# fix those with vpn issue

text = ['VPN','vpn','Vpn']
textCount = 0
changedCount = 0
unchangedtagq = []

for i in tagq:
    for t in text:
        if t in i['case.title']:
            textCount +=1
            if i['ms.service'] == 'virtual-network':
                i['ms.service'] = 'vpn-gateway'
                changedCount += 1
            elif i['ms.service'] != 'vpn-gateway':
                unchangedtagq.append(i)
                #print(i['ms.service'])

print(textCount," lines of caselog contains ", text)
print(changedCount, " lines of them was tagged to virtual-network and now into vpn-gateway")
print(len(unchangedtagq)," lines of them wad tagged neither virtual-network nor vpn-gateway.")
#printList(unchangedtagq)
#print("please look into those and see if there is any problems." )





destPath = "C:\\Users\\yuqwe\\Source\\Repos\\Mooncake CSS ChatBot\\data\\caselog\\"

# write cleaned csv

writeCsv(tagq,destPath+'cleaned_caselog.csv')
print(len(tagq), "lines of cleaned caselog is stored.")

# write vpn not changed csv to review
writeCsv(unchangedtagq,destPath+'need_review_unchanged_VPN_caselog.csv')
print(len(unchangedtagq), "lines of unchanged vpn caselog is stored and may need further review.")


# record duplicate caselog 
writeCsv(caselogFaqDict,destPath + 'need_review_caselog_duplication_aka_faq.csv')
print(len(caselogFaqDict), "lines of duplicate caselog as known as faq is stored and may need further review.")





