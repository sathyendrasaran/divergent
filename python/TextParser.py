# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:27:13 2016
@author: sathyendrasaran
"""
import nltk


# open a text file
f = open('../datasets/raven.txt')

# tokenize text file with nltk
words = nltk.word_tokenize(f.read().lower())
f.close()

# get frequent words
freq = nltk.FreqDist(words)
freq.plot(25)

stopwords = nltk.corpus.stopwords.words('english')
print stopwords


words2 = [w for w in words if w not in stopwords and len(w) > 1]
freq2 = nltk.FreqDist(words2)
print('raw text')
freq.plot(30)
print('text without stopwords')
freq2.plot(30)