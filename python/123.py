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
    
jnp=pd.io.json.read_json("C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Fall\\Data science\\HW\\grp 2\\pokemon_android_data.json")

date=[]
current_ratings=[]
all_ratings=[]
file_size=[]
oneRating=[]        
twoRating=[]
threeRating=[]
fourRating=[]
fiveRating=[] 
        
with open("C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Fall\\Data science\\HW\\grp 2\\pokemon_android_data.json","r") as file_object:
            data=json.load(file_object)
            for datum in data:
                date.append(datetime.strptime(datum, '%Y_%m_%d_%H_%M').strftime('%Y-%m-%d'))
                current_ratings.append(int(round(float(data[datum]["average_rating"]))))
                all_ratings.append(data[datum]["total_rating"].encode('utf-8'))
                file_size.append(str(data[datum]["file_size"]).replace("M","").encode('utf-8'))
                oneRating.append(data[datum]["rating_1"].encode('utf-8'))
                twoRating.append(data[datum]["rating_2"].encode('utf-8'))
                threeRating.append(data[datum]["rating_3"].encode('utf-8'))
                fourRating.append(data[datum]["rating_4"].encode('utf-8'))
                fiveRating.append(data[datum]["rating_5"].encode('utf-8'))

zdf=zip(current_ratings,file_size,oneRating,twoRating,threeRating,fourRating,fiveRating,all_ratings)

zpdf = pd.DataFrame(zdf, columns=['avg_rating', 'file_size', 'one_rating','two_rating','three_rating','four_rating','five_rating','all_ratings'])

lm = linear_model.LinearRegression()
axz=zpdf.dropna()
axz[['avg_rating', 'file_size', 'one_rating','two_rating','three_rating','four_rating','five_rating','all_ratings']] = axz[['avg_rating', 'file_size', 'one_rating','two_rating','three_rating','four_rating','five_rating','all_ratings']].apply(pd.to_numeric)
axz = axz[np.isfinite(axz['four_rating'])]

lm.fit(axz.drop('all_ratings',axis=1),axz['all_ratings'])

resultDf=pd.DataFrame(zip(axz.drop('all_ratings',axis=1),lm.coef_),columns=['features','estimates'])

resultDf

lm.intercept_

