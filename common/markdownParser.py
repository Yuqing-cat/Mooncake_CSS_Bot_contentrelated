# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:15:31 2018

@author: yuqwe
"""

import mistune
import re


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

# fine <hr> in content, split headContent and bodyContent
def getHeader(file, split = '<hr>\n'):
    a = file['contents']
    enumerate(a)
    headIndex = [i for i, x in enumerate(a) if x == split]
    startIndex = headIndex[0]+1
    endIndex = headIndex[1]
    headContent = a[startIndex:endIndex]
    #print(headContent)
    bodyContent = a[endIndex+1:] 
    file['bodyContent'] = bodyContent
    n = 0
    for i in headContent:
        x = re.findall(r'(?<=<p>).+?(?=</p>)',i)
        if x == []:
            continue
        else:
            x = x[0].split(":")
            key = x[0]
            value = x[1].replace("\"","")
            file[key] = value
            n= n +1
        #print(x)
    print(file['fileLocation'])
    print("This file has a header with {} metadata attibutes.".format(n))
    #print('title: ',file['title'])   
    #print('description: ',file['description'])  
    return file


def searchText(fileList,text = ['常见问题']):
    result = []
    for file in fileList:
        filename = file['fileName']
        content = file['contents']
        '''
        for i in content:
            for t in text:
                if t in i:
                    result.append(fileList.index(file))
                    print(i)
        '''
        if filename == 'index':
            print("this is an index.md file not qualified.")
        elif 'faq' in filename:
            result.append(fileList.index(file))
        else:
            if 'title' in file.keys():
                title = file['title']
                description = file['description']
                for t in text:
                    if t in filename or t in title or t in description:
                        result.append(fileList.index(file))
                        print(result)
            else:
                print("This file {} is not qualified. not index + no faq in title + no title meta".format(filename))  
    result = sorted(list(set(result)))
    print("there are {} files in list have text.".format(len(result)))
    print("?",result)
    return result
    
