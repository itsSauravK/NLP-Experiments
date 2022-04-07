#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:12:58 2022

@author: sauravkumar
"""
#https://classroom.google.com/u/2/c/NDUwOTk2NDQxODQz/m/NDUwOTk2NDQxODYw/details
#https://classroom.google.com/u/2/c/NDUwOTk2NDQxODQz/m/NDUwOTk2NDQxODc2/details
#Q14
import nltk
#nltk.download('tagsets')
nltk.download('averaged_perceptron_tagger')
  
sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens=nltk.word_tokenize(sent)

print(nltk.pos_tag(tokens))
nltk.help.upenn_tagset('.*')