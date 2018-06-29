# Mooncake_CSS_Bot_contentrelated
This repo contants raw code about Mooncake CSS Chatbot Content Extraction. 
And this Readme is regular tasks that is needed for content refresh.

### **Task: Refresh Chinses FAQ**

#### 1. extract faq content from file
#### 2. merge learned faq
#### 3. upload to blob storage

### **Task: Refresh KB Article (both Chinese & English)**
#### 1. git pull **a.cn content** 
#### 2. upload to blob storage
```
cd C:\Program Files (x86)\Microsoft SDKs\Azure\AzCopy
```
-  aog related: [] 
```
AzCopy /Source:D:\az-docs-pr.zh-cn /Dest:https://knowledgebasesaint.blob.core.windows.net/azure-operation-guide/articles/ /Pattern:"*.md" /DestKey:"STORAGE_KEY_HERE" /S

```
- [mc-docs-pr](https://github.com/wacn/mc-docs-pr.zh-cn/tree/live) 
- [mooncake docs](https://github.com/wacn/mc-docs-pr.zh-cn/tree/live)
- [mooncake docs](https://github.com/wacn/mc-docs-pr.en-us/tree/live)
- [azure docs with aog (chinese)](https://github.com/wacn/az-docs-pr.zh-cn/tree/live)
- [azure docs with aog (english)](https://github.com/wacn/az-docs-pr.en-us/tree/live)
- [marketing content (chinese)](https://github.com/wacn/acn-portal-pr.zh-cn/tree/live)
- [marketing content (english)](https://github.com/wacn/acn-portal-pr.en-us/tree/live)


### **Task: Process caselog**

*Need to run under Team repo*
```
python caselogProcessor.py
```

### **Task: Refresh English General FAQ**
#### 1. open powershell under local repo, e.g.:
```ps
cd C:\Users\yuqwe\Documents\GitHub\Mooncake_CSS_Bot_contentrelated
```
#### 2. run englishFAQextraction.ps1,e.g.:
```ps
.\englishFAQextraction.ps1
```
#### 3. upload to blob storage
```
cd C:\Program Files (x86)\Microsoft SDKs\Azure\AzCopy
AzCopy /Source:C:\Users\yuqwe\Documents\GitHub\Mooncake_CSS_Bot_contentrelated\EnglishFAQextraction /Pattern:"englishFaq.csv" /Dest:https://knowledgebasesaint.blob.core.windows.net/englishfaq/ /DestKey:"STORAGE_KEY_HERE"
```

