#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:52:55 2022

@author: sauravkumar
"""
#https://classroom.google.com/u/2/c/NDUwOTk2NDQxODQz/m/NDUwOTk2NDQxODc2/details
import spacy
 
nlp = spacy.load("en_core_web_sm")

sentence = 'Apple is looking at buying U.K. startup for $1 billion'

doc = nlp(sentence)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
