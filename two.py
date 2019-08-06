#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:02:02 2019

@author: Harsh
"""
# Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Create a list with the url
gb8tb1=["https://www.flipkart.com/dell-vostro-14-3000-core-i5-8th-gen-8-gb-1-tb-hdd-windows-10-home-3478-laptop/p/itmf8dhh38czg3vy?pid=COMF8DHHWE6YEAHF&lid=LSTCOMF8DHHWE6YEAHF2WU9JO&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_cb0ed1bf-238d-4711-8128-945648627b28_11_33033b38-3470-46f8-8da8-5e7173a25b22_DesktopSite_MC.COMF8DHHWE6YEAHF&ppt=clp&ppn=laptops-store&otracker=clp_pmu_v2_Laptops%2Bon%2BExchange_2_11.productCard.PMU_V2_Dell%2BVostro%2B14%2B3000%2BCore%2Bi5%2B8th%2BGen%2B-%2B%25288%2BGB%252F1%2BTB%2BHDD%252FWindows%2B10%2BHome%2529%2B3478%2BLaptop_laptops-store_COMF8DHHWE6YEAHF_neo%2Fmerchandising_1&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Laptops%2Bon%2BExchange_LIST_productCard_cc_2_NA_view-all&cid=COMF8DHHWE6YEAHF",
      "https://www.snapdeal.com/product/dell-vostro-3583-notebook-core/665988459890",
      "https://www.snapdeal.com/product/lenovo-ideapad-81lg0094in-notebook-core/624325181339#bcrumbSearch:laptops"]

gb4gb256=["https://www.flipkart.com/hp-pavilion-x360-core-i3-8th-gen-4-gb-256-gb-ssd-windows-10-home-14-dh0107tu-2-1-laptop/p/itmffevzx5tacuw8?pid=COMFFG4HPFUCQ2HF&srno=b_1_6&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_HP_laptops-store_ZCQFAP2R5I_wp4&lid=LSTCOMFFG4HPFUCQ2HFRFMNZB&fm=organic&iid=aa4a0769-c3be-4ec0-a1a3-963c6ca19433.COMFFG4HPFUCQ2HF.SEARCH",
          "https://www.flipkart.com/asus-vivobook-14-core-i3-7th-gen-4-gb-256-gb-ssd-windows-10-home-x412ua-ek341t-thin-light-laptop/p/itmfg9yrgwqt7dn5?pid=COMFG9YRYY4TDEH4&srno=b_1_5&otracker=clp_metro_expandable_5_5.metroExpandable.METRO_EXPANDABLE_ASUS_laptops-store_O0C88CIUID_wp4&lid=LSTCOMFG9YRYY4TDEH4H1QNOH&fm=organic&iid=9b3cda03-4d97-4e3d-9e44-59d0fcfe1bac.COMFG9YRYY4TDEH4.SEARCH",
          "https://www.flipkart.com/dell-inspiron-14-5000-series-core-i3-8th-gen-4-gb-1-tb-hdd-windows-10-home-5482-2-1-laptop/p/itmfbygrqbacwbxa?pid=COMFBYGRFTUGR9GR&srno=b_1_9&otracker=clp_metro_expandable_2_5.metroExpandable.METRO_EXPANDABLE_Dell_laptops-store_LVL7DAHQW9_wp4&lid=LSTCOMFBYGRFTUGR9GRVIYVRE&fm=organic&iid=ee293f8f-6622-4a57-b45e-e05e9005b1e9.COMFBYGRFTUGR9GR.SEARCH"]

dummy=[0,0,1,0,1,0,0]
     
titles= []   
for url in gb4gb256:

    # Use requests to get the contents
    r = requests.get(url,verify=False)
    # Get the text of the contents
    html_content = r.text
    # Convert the html content into a beautiful soup object
    soup = BeautifulSoup(html_content, 'lxml')
    # View the title tag of the soup object
    titles.append(soup.title.string)
        
keywords=[]
if any("4 GB" in gb4 for gb4 in titles):
    keywords.append("4GB")
    
if any("8 GB" in gb8 for gb8 in titles):
    keywords.append("8GB")
    
if any("16 GB" in gb16 for gb16 in titles):
    keywords.append("16GB")
    
if any("256 GB" in gb256 for gb256 in titles):
    keywords.append("256GB")
    
if any("512 GB" in gb512 for gb512 in titles):
    keywords.append("512GB")    

if any("1 TB" in tb1 for tb1 in titles):
    keywords.append("1TB")    
    
if any("2 TB" in tb2 for tb2 in titles):
    keywords.append("2TB") 
    
laptops= pd.read_csv("dell_data_less.csv")
laptops=pd.concat([laptops,laptops['ATTRIBUTE'].str.get_dummies(sep=" ")],axis=1)
del laptops['ATTRIBUTE']
    
X =laptops.iloc[:,2:13]
      
list2=[]
for col in X:
    if col in keywords:
        list2.append(1)
    else:
        list2.append(0)

nbrs = NearestNeighbors(n_neighbors=3).fit(X)

result = (nbrs.kneighbors([list2]))[1]
result = result+1



