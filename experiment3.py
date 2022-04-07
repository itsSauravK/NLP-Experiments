#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:45:58 2022

@author: sauravkumar
"""

#https://classroom.google.com/u/2/c/NDUwOTk2NDQxODQz/m/NDUwOTk2NDQxODYw/details
#Q10-Q13
import nltk
import re
#analyze web page
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import urllib.request
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()

#print(html)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)

#punctuation and number removing
text = re.sub(r'[?:;''\'"%$[\]{},.()0-9]','',text)

print(text)

#tokenizing
tokens = word_tokenize(text)


#stopwords
sr= stopwords.words('english')
clean_tokens = []
#print (clean_tokens)
for token in tokens:
    if token not in stopwords.words('english'):
        clean_tokens.append(token)
        
#Plotting        
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(30, cumulative=False)
