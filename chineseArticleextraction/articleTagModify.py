# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 16:40:14 2018

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

import csv

import traverseFunction as x
import markdownParser as y
import csvReadWrite as z



def multicsvToDict(fileLocationList, headers,header =True):
    #fileLocationList = fileList
    #header = True
    rows = []
    dicts = []
    for fileLocation in fileLocationList:
        print('  Uploading from ',fileLocation)
        with open(fileLocation,'r',newline="", encoding = "utf-8") as f:
            reader = csv.reader(f)
            if header == True:
                # to skip header
                next(reader,None)
                print("\t header is ignored.")
            else:
                print("\t the csv file is set as no-header.")
            csv_dict = {}
            i = 0
            #print(reader)
            for row in reader:
                #print(row)
                l = 0
                csv_dict = {}
                while l < len(headers):
                    #print(i,'\t',l,'\t',row[l])
                    csv_dict[headers[l]] = row[l]
                    l+=1
                #print(row[1])
                rows.append(row)
                dicts.append(csv_dict)
                i = i+ 1
        print('\t',i, ' rows of data in loaded into python')
    return dicts




aogCategory = codePath + "\\aogCategory.csv"
kcCategory = codePath + "\\kcCategory.csv"
caselog = "D:\\GitHub\\Mooncake_CSS_Bot_contentrelated\\caselogProcessor\\cleaned_caselog.csv"
articleFalseTag = codePath + "\\articleFalseTag.csv"


# trasnform csv into dictionary
fileList = [aogCategory,kcCategory,caselog]
headers = ['title','description','ms.service']



articleCat = multicsvToDict(fileList,headers, True)
print(len(articleCat), " lines of rawdata is ready for modify")
falseTag = z.csvToDict(articleFalseTag,['false_tag','ms.service'],True)

# replace " " in article ms.service
for a in articleCat:
    a['ms.service'] = a['ms.service'].replace(" ","")
    
# replace "| Azure"
for a in articleCat:
    a['title'] = a['title'].replace(" | Azure","")
    

# remove ignore tag which ms.service tag is not 
ignoreTag = ['NA','monitoring-and-diagnostics','multiple','azure-resource-manager','na','best-practice','visual-studio-online','guidance','dns']
z.removeTag(articleCat,ignoreTag,'ms.service')
   


# corect Tag
for a in articleCat:
    for b in falseTag:
        if a['ms.service'] == b['false_tag']:
            a['ms.service'] = b['ms.service']
            print(a, "tag changed from",b['false_tag'])
        
print("article tag corrected recordding to falseTag csv.")

#aogTitle = z.subDict(articleCat,['title','ms.service'])
#aogDescription= z.subDict(articleCat,['description','ms.service'])

# write csv
destPath = "D:\\GitHub\\Mooncake_CSS_Bot_contentrelated\\chineseArticleextraction\\"
z.writeCsv(articleCat,destPath+'cleaned_articleCategory.csv')
print("article title and description is write into cleaned_articleCategory.csv with its ms.service tag")

#z.writeCsv(aogTitle,destPath+'aogTitle.csv')
#print("aog title is write into aogTitle.csv with its ms.service tag")