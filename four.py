#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:47:55 2019

@author: Harsh
"""

import pandas as pd
from sklearn.neighbors import NearestNeighbors

inputs= pd.read_csv("input.csv")
inputs=pd.concat([inputs,inputs['ATTRIBUTE'].str.get_dummies(sep=" ")],axis=1)
inputs = inputs[inputs.TIME > 5]

Y =inputs.iloc[:,3:13]

Keywords=list(Y.columns.values.tolist())

laptops= pd.read_csv("dell_data_less.csv")
laptops=pd.concat([laptops,laptops['ATTRIBUTE'].str.get_dummies(sep=" ")],axis=1)
X =laptops.iloc[:,3:13]
      
list2=[]
for col in X:
    if col in Keywords:
        print(col)
        list2.append(1)
    else:
        list2.append(0)
        
nbrs = NearestNeighbors(n_neighbors=3).fit(X)

result = (nbrs.kneighbors([list2]))[1]
result = result+1
