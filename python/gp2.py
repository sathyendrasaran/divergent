# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 13:48:34 2016

@author: sathyendrasaran
"""

import os
from bs4 import BeautifulSoup
from datetime import datetime
import pandas
import matplotlib.pyplot as plt
import json
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

class PokemonGoAndroidExtract():

    def getFileData(self):
        folderContentsDict=dict()
        for path, subdirs, files in os.walk(os.getcwd()+'\\data'):                      
           for filename in files:               
             if filename.endswith('android.html'):
                 f = os.path.join(path, filename)
                 dateKey=path.split("\\")[-1].replace("-","_")+"_"+filename.replace("_pokemon_android.html","")
                 folderContentsDict[dateKey]=self.parseHtml(f)                 
               
        with open("pokemon_android_data.json", "a") as androidJson:
            json.dump(folderContentsDict,androidJson,indent=4)

    def isNotNone(self,element):
        if element != None:
            return element.get_text()
        else:
            return 0
            
    def parseHtml(self,fileName):
    
        soup = BeautifulSoup(open(fileName))
        fileDict=dict()
        #print type(soup)       
        avgRating = soup.find("div", { "class" : "score" })
        totalRating = soup.find("span", { "class" : "reviews-num" })
        totalPerRating = soup.find_all("span", { "class" : "bar-number" })
        fileSize = soup.find("div", { "class" : "content","itemprop" : "fileSize"})
        version = soup.find("div", { "class" : "content","itemprop" : "softwareVersion"})
        description = soup.find("div", { "jsname" : "C4s9Ed" })            
        
        try:
            fileDict['average_rating']=self.isNotNone(avgRating)
        except:
            fileDict['average_rating']=""
        try:
            fileDict['total_rating']=str(self.isNotNone(totalRating)).replace(",","")
        except:            
            fileDict['total_rating']=""
        try:
            fileDict['rating_1']=str(self.isNotNone(totalPerRating[4])).replace(",","")
        except:
            fileDict['rating_1']=""            
        try:
            fileDict['rating_2']=str(self.isNotNone(totalPerRating[3])).replace(",","")
        except:
            fileDict['rating_2']=""            
        try:
            fileDict['rating_3']=str(self.isNotNone(totalPerRating[2])).replace(",","")
        except:
            fileDict['rating_3']=""
        try:
            fileDict['rating_4']=str(self.isNotNone(totalPerRating[1])).replace(",","")
        except:
            fileDict['rating_4']=""
        try:
            fileDict['rating_5']=str(self.isNotNone(totalPerRating[0])).replace(",","")
        except:
            fileDict['rating_5']=""
        try:
            fileDict['version']=self.isNotNone(version)
        except:
            fileDict['version']=""                        
        try:
            fileDict['file_size']=self.isNotNone(fileSize)           
        except:
            fileDict['file_size']=""
        try:
            fileDict['description']=self.isNotNone(description)
        except:
            fileDict['description']=""
            
        return fileDict
                                
            #print(Exception)
            
        
#        print(avgRating.get_text())
#        print(totalRating.get_text())        
#        print(totalPerRating[0].get_text())
#        print(totalPerRating[1].get_text())
#        print(totalPerRating[2].get_text())
#        print(totalPerRating[3].get_text())
#        print(totalPerRating[4].get_text())
#        print(fileSize.get_text())        
#        print(description.get_text())
        
        
    def plot_graph(self):
        date=[]
        current_ratings=[]
        all_ratings=[]
        file_size=[]
        oneRating=[]        
        twoRating=[]
        threeRating=[]
        fourRating=[]
        fiveRating=[] 
        
        with open("pokemon_android_data.json","r") as file_object:
            data=json.load(file_object)
        for datum in data:
            date.append(datetime.strptime(datum, '%Y_%m_%d_%H_%M').strftime('%Y-%m-%d'))
            current_ratings.append(float(data[datum]["average_rating"]))
            all_ratings.append(data[datum]["total_rating"].encode('utf-8'))
            file_size.append(str(data[datum]["file_size"]).replace("M","").encode('utf-8'))
            oneRating.append(data[datum]["rating_1"].encode('utf-8'))
            twoRating.append(data[datum]["rating_2"].encode('utf-8'))
            threeRating.append(data[datum]["rating_3"].encode('utf-8'))
            fourRating.append(data[datum]["rating_4"].encode('utf-8'))
            fiveRating.append(data[datum]["rating_5"].encode('utf-8'))

#            print all_ratings
            
            
        self.plt_grp(date,current_ratings,'Current Ratings')
        #self.plt_grp(date,all_ratings,'All Ratings')
        #self.plt_grp(date,file_size,'File Size')
        #self.plt_grp(date,oneRating,'Ratng One')
        #self.plt_grp(date,twoRating,'Rating Two')
        #self.plt_grp(date,threeRating,'Rating Three')
        #self.plt_grp(date,fourRating,'Rating Four')
        #self.plt_grp(date,fiveRating,'Rating Five')
        
        
    def plt_grp(self,xlist,ylist,name):
        yaxis=[]
        
        for x in ylist:
            if x=='':
                x=0
            yaxis.append(int(x))
        
        df=pandas.DataFrame({'Date':xlist,name:yaxis})
        print df
        df=df[df[name]!=0]
        pandas.to_datetime(df['Date'],format="%Y-%m-%d")
        
        df=df.sort_values(['Date'])
        padding=min(df[name])-(max(df[name])-min(df[name]))%10
        df.plot(x='Date',figsize=(20,10),ylim=(min(df[name])-padding,max(df[name])+padding))




        