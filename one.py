#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 02:14:21 2019

@author: Harsh
"""

import pandas as pd
from sklearn.neighbors import NearestNeighbors

laptops= pd.read_csv("dell_data_less.csv")
laptops=pd.concat([laptops,laptops['ATTRIBUTE'].str.get_dummies(sep=" ")],axis=1)
del laptops['ATTRIBUTE']

inputs= pd.read_csv("input.csv")
inputs=pd.concat([inputs,inputs['ATTRIBUTE'].str.get_dummies(sep=" ")],axis=1)
del inputs['ATTRIBUTE']

X =laptops.iloc[:,2:13]

list1=[]
for col in inputs.columns:
    if col!='PID' and col!='PNAME':
        list1.append(col)
        
list2=[]
for col in X:
    if col in list1:
        list2.append(1)
    else:
        list2.append(0)

nbrs = NearestNeighbors(n_neighbors=3).fit(X)

print(nbrs.kneighbors([list2]))
