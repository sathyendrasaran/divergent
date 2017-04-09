# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:02:02 2016

@author: sathyendrasaran
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:40:51 2016

@author: sathyendrasaran
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from datetime import datetime
import pandas as pd
import json

with open("C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Fall\\Data science\\HW\\grp 2\\pokemon_android_data.json","r") as file_object:
     data=json.load(file_object)
    
jnp=pd.io.json.read_json("C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Fall\\Data science\\HW\\grp 2\\pokemon_ios.json")

date=[]
current_ratings=[]
all_ratings=[]
file_size=[]
version=[]        
twoRating=[]
threeRating=[]
fourRating=[]
fiveRating=[] 
        
with open("C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Fall\\Data science\\HW\\grp 2\\pokemon_ios.json","r") as file_object:
            data=json.load(file_object)
            for datum in data:
                date.append(datetime.strptime(datum, '%Y-%m-%d_%H_%M').strftime('%Y-%m-%d'))
                current_ratings.append(data[datum]["total_rating_current_version"])
                all_ratings.append(data[datum]["total_rating"].encode('utf-8'))
                file_size.append(str(data[datum]["file_size"]).replace("M","").encode('utf-8'))
                version.append(str(data[datum]["version"]).replace(".",""))
                
zdf=zip(current_ratings,file_size,version,all_ratings)

zpdf = pd.DataFrame(zdf, columns=['tot_curr_rating', 'file_size', 'version','all_ratings'])

lm = linear_model.LinearRegression()
axz=zpdf.dropna()
axz[['tot_curr_rating', 'file_size', 'version','all_ratings']] = axz[['tot_curr_rating', 'file_size', 'version','all_ratings']].apply(pd.to_numeric)
axz = axz[np.isfinite(axz['tot_curr_rating'])]

lm.fit(axz.drop('all_ratings',axis=1),axz['all_ratings'])

resultDf=pd.DataFrame(zip(axz.drop('all_ratings',axis=1),lm.coef_),columns=['features','estimates'])
resultDf
lm.intercept_