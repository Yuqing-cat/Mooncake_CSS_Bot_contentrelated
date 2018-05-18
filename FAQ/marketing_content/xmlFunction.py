import xml.etree.cElementTree as ET
import os

def getXmlLocation(dir,preurl):
    # the list of all urls 
    urlList = []
    # the list of all file location
    fileList = []
    # list of product names
    products = []
    for root,dirs,files in os.walk(dir):
        for file in files:
            # file location generate
            # print(os.path.join(root,file))
            fileLocation = os.path.join(root,file)
            #print("this file location is:\n",fileLocation)
            fileList.append(fileLocation)
            # split endurl from file location
            url_temp = fileLocation.split("\\")
            #print("split file location: ",url_temp)
            url_temp[-1] = (url_temp[-1].split("."))[0]
            #print("remove file type: ",url_temp)
            del url_temp[0:4]
            #print("remove location dir",url_temp)
            endurl = "/".join(url_temp)
            #print("endurl is: ", endurl)
            # product list generation
            product = "-".join(url_temp[2:])
            #print("this product is:\n",product)        
            products.append(product)
            # generate url
            urls = preurl+endurl+'/'
            #print("article external url is:\n",urls)
            urlList.append(urls)
            print("A file named {} is extracted, {} files is already extracted.".format(product,len(products)))
    print("%s files is found under this dir and all extraction is done"%len(urlList))
    return urlList,fileList,products




# get ccertain tag ontent from xmlText
def getXmlContent(fileList,tags=['pageTitle','mataDescription']):
    count = 0
    contents = []
    for file in fileList:
        #print(file)
        xmlTree = ET.parse(file)
        xmlRoot = xmlTree.getroot()

        count = count+1
        #print(count)
        for child in xmlRoot:
            content = getXmlText(child,tags)
        contents.append(content)
    print('There are {} articles in this list, {} of them has {} content is as followed:'.format(count,len(contents),tags))
    print(contents)
    return contents
    
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