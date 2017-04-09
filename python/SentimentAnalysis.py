# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 16:32:46 2016

@author: sathyendrasaran
"""

from textblob import TextBlob
from textblob import Word

s_pos = 'this is a great class'
s_neg = 'this is not a great class'
tb_pos = TextBlob(s_pos)
tb_neg = TextBlob(s_neg)
print(tb_pos.sentiment)
print(tb_neg.sentiment)

b = TextBlob("I havv goood speling!")
print(b.correct())
b=b.correct()
print(b)
print(b.tags)
print(b.sentiment)


w = Word('goode')
w.spellcheck()


# open a text file
f = open('../datasets/raven.txt')
lines = f.read().split('.')
f.close()

three_long_lines = []
for line in lines:
    words = line.strip().split()
    if len(words) > 10:
        three_long_lines.append(line.rstrip())
    if len(three_long_lines) >= 3:
        break

for line in three_long_lines:
    tb = TextBlob(line)
    print '\nactual text\n', line
    print '\nwords\n', tb.words
    print '\ntags\n', tb.tags
    print '\nsentiments\n', tb.sentiment
    print