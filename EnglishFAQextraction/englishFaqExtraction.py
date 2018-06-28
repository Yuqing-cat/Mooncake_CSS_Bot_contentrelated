# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:07:57 2018

this file is to extract english faq from content

@author: yuqwe
"""


import xml.etree.cElementTree as ET
import csv

# get Text from xml sub.text
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

#extract from 
url = "https://www.azure.cn/en-us/support/faq"
rootPath = "C:\\Users\\yuqwe\\Documents\\GitHub\\acnContent\\"
midPath = "acn-portal-pr.en-us\\acn-resources\\en-required\\"
fileName = "support,faq.xml"

fileLocation = rootPath + midPath + fileName

contents = []
xmlTree = ET.parse(fileLocation)
xmlRoot = xmlTree.getroot()
tags = ['bodyText']
for child in xmlRoot:
    content = getXmlText(child,tags)
    contents.append(content)
    
print(contents)


import re
for i in contents:
    m = i['bodyText'] 
    ids = re.findall('<a id="(.*)" href="#(.*)">(.*)</a>',m)
questions = []
countnq = 0
countq = 0
for q in ids:
    if q[1] == '':
        countnq = countnq + 1
        #print("nq",q[1])
    else:
        #print("q",q[1])
        countq = countq + 1
        questions.append(q[1])
print("there are", countq, " questions")
print("they are: ",questions)


for i in contents:
    categoryQ = re.split('<h2>',m)


qnaList = []
for i in range(2,6):
    category = categoryQ[i].split('</h2>')[0]
    print(category)
    
    texts = categoryQ[i].split('</h2>')[1]
    # split text into qnas
    a = re.split('<i class="icon icon-plus"></i>',texts)
    #print(a)

    # split qna into q and a and id
    for q in a:
        question = re.findall('href="#(.*)">(.*)</a>',q)
        answer = re.split('</section>',q)[0]
        answer = re.split('<section>',answer)
        qna = {}
        print(len(question),len(answer))
        if len(answer) >= 2:
            print(question,answer[1])
            #qna['id'] = question[0][0]
            qna['question'] = question[0][1]
            raw_answer = re.findall(r'(?<=<p>).+?(?=</p>)',answer[1])
            qna['answer'] = "\n\n".join(raw_answer)
            qna['category'] = category
            qna['source'] = url + '#' + question[0][0]
            qnaList.append(qna)

print(len(qnaList),"qna pairs is extracted.")    

    
# write qnaList into csv file
destFile = 'C:\\Users\\yuqwe\\Documents\\GitHub\\Mooncake_CSS_Bot_contentrelated\\EnglishFAQextraction\\englishFaq.csv'

with open(destFile,'w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(qnaList[0].keys())
    for i in qnaList:
        w.writerow(i.values())
    
            

    

