#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:49:06 2022

@author: sauravkumar
"""

import nltk #nltk.download('averaged_perceptron_tagger') # #nltk.download('sentiwordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('sentiwordnet')
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn 
from nltk.stem import PorterStemmer

def penn_to_wn(tag):
# Convert between the PennTreebank tags to simple Wordnet tags 
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'): 
        return wn.NOUN
    elif tag.startswith('R'): 
        return wn.ADV
    elif tag.startswith('V'): 
        return wn.VERB

    return None

from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()

def get_sentiment(word,tag):
# returns list of pos neg and objective score. But returns empty list if not present in senti wordnet.
    wn_tag = penn_to_wn(tag)
    if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV): 
        return []
    lemma = lemmatizer.lemmatize(word, pos=wn_tag) 
    if not lemma:
        return []
    synsets = wn.synsets(word, pos=wn_tag) 
    if not synsets:
        return []

# Take the first sense, the most common 
    synset = synsets[0]
    swn_synset = swn.senti_synset(synset.name()) 
    return [swn_synset.pos_score(),swn_synset.neg_score(),swn_synset.obj_score()]

ps = PorterStemmer()
words_data = ['this','movie','is','wonderful']
# words_data = [ps.stem(x) for x in words_data] # if you want to further stem the word
pos_val = nltk.pos_tag(words_data)
senti_val = [get_sentiment(x,y) for (x,y) in pos_val] 
print(f"pos_val is {pos_val}")
print(f"senti_val is {senti_val}")


