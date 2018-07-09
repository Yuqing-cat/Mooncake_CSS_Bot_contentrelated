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


import traverseFunction as x
import markdownParser as y
import csvReadWrite as z






articleCategory = codePath + "\\articleCategory.csv"
articleFalseTag = codePath + "\\articleFalseTag.csv"

articleCat = z.csvToDict(articleCategory,['title','description','ms.service'], True)
falseTag = z.csvToDict(articleFalseTag,['false_tag','ms.service'],True)

# replace " " in article ms.service
for a in articleCat:
    a['ms.service'] = a['ms.service'].replace(" ","")

# remove ignore tag which ms.service tag is not 
ignoreTag = ['NA','monitoring-and-diagnostics','multiple']
z.removeTag(articleCat,ignoreTag,'ms.service')
   


# corect Tag
for a in articleCat:
    for b in falseTag:
        if a['ms.service'] == b['false_tag']:
            a['ms.service'] = b['ms.service']
            print(a, "tag changed from",b['false_tag'])
        
print("article tag corrected recordding to falseTag csv.")

articleTitle = 

article
# write csv
destPath = "D:\\GitHub\\Mooncake_CSS_Bot_contentrelated\\chineseArticleextraction\\"
z.writeCsv(articleMeta,destPath+'artileTitle.csv')