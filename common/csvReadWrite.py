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