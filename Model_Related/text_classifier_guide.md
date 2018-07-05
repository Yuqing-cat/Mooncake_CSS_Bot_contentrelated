# KnowledgeBot Classifier Training Process

This file describes how to setup training environment, prepare requirement and train a Knowledge bot classifier model

## Environmnent setup

* VM: Ubuntu Server 18.04 LTS
* Size: Standard E16s v3 (16 vcpus, 128 GB memory) at least 64G is need right now,

## Requirements

* pip
* python packages
  * ```sudo pip install analytics*zoo```
  * ```sudo pip install cython```
  * ```sudo pip install pyspark```
  * ```sudo pip install jieba```
  * ```sudo pip install sklearn```
  * ```sudo pip install scipy```
  * ```sudo apt install openjdk*8*jdk ```
* sample code
  * ```git clone git@github.com:intel*analytics/KnowledgeBotPoC.git```
* word vector model (7G):
  * ```wget http://13.75.122.244/cc.zh.300.bin ```
* upload caselog file; update qna file.  

## Model training

* run text_classification.py
  * ```cd KnowledgeBotPoC/train/classifier```
  * ```export SPARK_DRIVER_MEMORY=35g```
  * ```python text_classification.py *-qa_path ~/KnowledgeBotPoC/data/trainingMaterials/faq/modifiedquestionv3_20180613.csv --caselog_path ~/cleaned_caselog.csv --fasttext_path ~/cc.zh.300.bin```
* get model
  * ```cd tmp\models```

## Notice

Currently, the script would run about 20 minutes with 20 epochs. 

tips:
* DSVM Linux(centOS) has too many tricks 
* Memory too small (e.g. 16G) will lead to failure
* Remember to install all python package