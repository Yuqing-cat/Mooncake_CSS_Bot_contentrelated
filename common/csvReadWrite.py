# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:24:38 2018

@author: yuqwe
"""
import csv

def writeCsv(sourceList, destFile):
    with open(destFile,'w',newline='',encoding = 'utf-8') as f:
        w = csv.writer(f)
        w.writerow(sourceList[0].keys())
        for i in sourceList:
            w.writerow(i.values())
            

# trasnform csv into dictionary
def csvToDict(fileLocation, headers,header =True):
    rows = []
    dicts = []
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
        
        
def removeTag(contentList,ignoreTag,dictKey):
    print('before remove: ',len(contentList), 'lines of data')
    for tag in ignoreTag:
        i = 0
        while i < len(contentList):
            if contentList[i][dictKey] == tag:
                del contentList[i]
            else:
                i += 1
    print('after remove: ',len(contentList),'lines of data')