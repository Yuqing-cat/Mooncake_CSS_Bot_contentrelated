# -*- coding: utf-8 -*-
"""
Created on Wed May 23 21:27:46 2018

@author: yuqwe
"""
import xlrd

faq_learned = "C:\\Users\\yuqwe\\Documents\\GitHub\\Mooncake_CSS_Bot_contentrelated\\FAQ\\faq_csv\\faq_learned.xlsx"
excelFile = xlrd.open_workbook(faq_learned)
print(excelFile.sheet_names())

sheet = excelFile.sheet_by_index(0)
print(sheet.name,sheet.nrows,sheet.ncols)

for i in range(0,sheet.nrows):
    print(sheet.row_values(i))