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
        source = fileLocation.split("\\")[-1]
        with open(fileLocation,'r',newline="", encoding = "utf-8") as f:
            reader = csv.reader(f)
            if header == True:
                # to skip header
                next(reader,None)
                print("\t header is ignored.")
            else:
                print("\t the csv file is set as no-header.")
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
                csv_dict['source'] = source
                rows.append(row)
                dicts.append(csv_dict)
                i = i+ 1
        print('\t',i, ' rows of data in loaded into python')
    return dicts




aogCategory = codePath + "\\aogCategory.csv"
kcCategory = codePath + "\\kcCategory.csv"
caselog = codePath + "\\cleaned_caselog.csv"
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
print(len(articleCat), " lines of ms.service tag corrected data is ready for cleaning")
#aogTitle = z.subDict(articleCat,['title','ms.service'])
#aogDescription= z.subDict(articleCat,['description','ms.service'])

# write csv
cleand_articleCategory = z.subDict(articleCat, ['title','description','ms.service'])
destPath = codePath
z.writeCsv(cleand_articleCategory,destPath+'cleaned_articleCategory.csv')
print("article title and description is write into cleaned_articleCategory.csv with its ms.service tag")

#z.writeCsv(aogTitle,destPath+'aogTitle.csv')
#print("aog title is write into aogTitle.csv with its ms.service tag")


# add description
print("%s lines of data is in articleCat"% len(articleCat))
descriptionContent = []
for a in articleCat:
    descriptionDict = {}
    if a['description'] == 'NA':
        break
    elif a['source'] == 'cleaned_caselog.csv':
        break
    elif a['source'] == 'aogCategory.csv':
        descriptionDict['description'] = a['title']
        descriptionDict['title'] = a['description']
        descriptionDict['ms.service'] = a['ms.service']
        descriptionDict['source'] = 'aog_description'
        
    elif a['source'] == 'kcCategory.csv':
        descriptionDict['description'] = a['title']
        descriptionDict['title'] = a['description']
        descriptionDict['ms.service'] = a['ms.service']
        descriptionDict['source'] = 'kc_description'
    descriptionContent.append(descriptionDict)
print('%s lines of description is in description content' % len(descriptionContent))

# remove duplicate content

for d in descriptionContent:
    if d in articleCat:
        print(articleCat.index(d),"has ", d)
    else:
        articleCat.append(d)
        #print("add d")
print("%s lines of data is in articleCat"% len(articleCat))  

cleaned_articleCategory_withDescription = z.subDict(articleCat, ['title','source','ms.service'])

destPath = codePath
z.writeCsv(cleaned_articleCategory_withDescription,destPath+'\\cleaned_articleCategory_withDescription.csv')
print("article title and description is write into cleaned_articleCategory_withDescription.csv with its ms.service tag")
