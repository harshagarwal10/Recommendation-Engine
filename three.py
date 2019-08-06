#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:50:41 2019

@author: Harsh
"""
# Import required modules
import pandas as pd
from sklearn.neighbors import NearestNeighbors

keywords =[ "512GB","512GB","512GB","512GB","256GB","8GB","8GB","4GB","4GB","4GB","40K","55K",
           "40K","40K","40K","14.5","14.5","17.3","17.3","14.5"]

unique = list(set(keywords))
optimum=[]

for val in unique:
    count = keywords.count(val)
    if count >= 5:
        optimum.append(val)
        
for val in unique:
    count = keywords.count(val)
    if count < 2:
        unique.remove(val)

if len(optimum) != 0:
    unique = optimum
    
laptops= pd.read_csv("dell_data_less.csv")
laptops=pd.concat([laptops,laptops['ATTRIBUTE'].str.get_dummies(sep=" ")],axis=1)
del laptops['ATTRIBUTE']  
    
X =laptops.iloc[:,2:13]
      
list2=[]
for col in X:
    if col in unique:
        list2.append(1)
    else:
        list2.append(0)
        
nbrs = NearestNeighbors(n_neighbors=3).fit(X)

result = (nbrs.kneighbors([list2]))[1]
result = result+1
