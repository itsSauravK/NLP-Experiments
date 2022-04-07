#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:25:23 2022

@author: sauravkumar
"""
#https://classroom.google.com/u/2/c/NDUwOTk2NDQxODQz/m/NDUwOTk2NDQxODYw/details
#Q15
import nltk
nltk.download('words')
import re
wordlist = [w for w in nltk.corpus.words.words('en') ]
#print(wordlist)
print([w for w in wordlist if re.search('ed$', w)])


import nltk
import re
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
print([w for w in wordlist if re.search('^..j..t..$', w)])

