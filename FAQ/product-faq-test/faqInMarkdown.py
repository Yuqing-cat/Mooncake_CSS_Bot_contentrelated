# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:54:06 2018

@author: yuqwe
"""
import sys
import traverseFunction as x
import markdownParser as y 
import csv

dir = "C:\\Users\\yuqwe\\Documents\\GitHub\\az-docs-pr.zh-cn\\"

# dir exist
x.dirExist(dir)

# set parameters
suffix = '.md'

# get all markdown files from selected folders
fileList, fileName, fileInfo = x.findSuffix(dir,suffix)

# generate url
preurl = 'https://docs.azure.cn/zh-cn/'
for file in fileInfo:
    print(file['fileLocation'])
    file['URL'] = x.getUrl(file['fileLocation'],preurl)


# extract markdown content.
i = 0
for file in fileInfo: 
    y.getContent(file)
    split = '<hr>\n'
    #print(i,file['fileName'],file['fileLocation'])
    i = i + 1
    # extract header info from content.
    if split in file['contents']:
        file = y.getHeader(file)
    else:
        print("not include header")
print(i,"file cotent extraction done.")

# search faq related files 
text = ['常见问题','faq','FAQ']
textIndex = y.searchText(fileInfo,text)

'''
for i in textIndex:
    print(fileInfo[i]['title'])
    print(fileInfo[i]['fileName'])
    print(fileInfo[i]['URL'])
'''
# write faq urls into faqURL.csv
faqUrlList = "C:\\Users\\yuqwe\\Documents\\GitHub\\Mooncake_CSS_Bot_contentrelated\\FAQ\\faqURL.csv"
with open(faqUrlList, encoding='utf-8',mode='w',newline = '') as f:
    w = csv.writer(f)
    for i in textIndex:
        w.writerow([fileInfo[i]['URL']])
f.close()

# try to parse QnA pair from content
    i = textIndex[0]
    print(fileInfo[i]['title'])
    print(fileInfo[i]['fileName'])
    print(fileInfo[i]['URL'])
    print(fileInfo[i]['contents'])
 


'''
def searchText(fileList,text = ['常见问题']):
    result = []
    for file in fileList:
        filename = file['fileName']
        content = file['contents']
        for i in content:
            for t in text:
                if t in i:
                    result.append(fileList.index(file))
                    print(i)
        
        if 'title' in file.keys():
            title = file['title']
            description = file['description']
            for t in text:
                if t in title or t in description:
                    result.append(fileList.index(file))
                    print(result)
        else:
            print("This file {} is not qualified.".format(filename))
        
    result = sorted(list(set(result)))
    print("there are {} files in list have text.".format(len(result)))
    return result



############## test in specific file     
# extract markdown content 
file = fileInfo[14]

    
def getContent(file):
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
            #print(i,":",content)
            contents.append(content)
    file['contents'] = contents
    #print(file)
    print("{} markdown content has been extracted into file['contents']".format(filename))
    print("content length is {}\n".format(len(contents)))
    return file

# fine <hr> in content
def getHeader(file, split = "<hr>\n"):
    a = file['contents']
    enumerate(a)
    headIndex = [i for i, x in enumerate(a) if x == split]
    startIndex = headIndex[0]+1
    endIndex = headIndex[1]
    headContent = a[startIndex:endIndex]
    #print(headContent)
    n = 0
    for i in headContent:
        x = re.findall(r'(?<=<p>).+?(?=</p>)',i)
        #print(i,x)
        if x == []:
            continue
        else:
            x = x[0].split(":")
            key = x[0]
            value = x[1]
            file[key] = value
            n= n +1
        #print(x)
    print(file['fileLocation'])
    print("This file has a header with {} metadata attibutes.".format(n))
    print('title: ',file['title'])   
    print('description: ',file['description'])  
    return file


    getContent(file)
    split = "<hr>\n"
    file = getHeader(file,split)









# deprecated. 

    
    
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