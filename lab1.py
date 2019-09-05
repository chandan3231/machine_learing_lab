# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:19:51 2019
@author: Student
"""
import csv
with open("C:\\deepa\\findss.csv") as find:
    reader=csv.reader(find)
    data=list(reader)
len(data)
h=['0','0','0','0','0','0']
for row in data:
    if row[-1] == 'Yes' :
        j=0
        for col in row:
            if col!='Yes':
                if col!=h[j] and h[j]=='0':
                    h[j]=col
                elif col!=h[j] and h[j]!='0':
                        print(col)
                        h[j]='?'
            j=j+1
print(h)