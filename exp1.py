#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:00:56 2022

@author: sauravkumar
"""
#https://classroom.google.com/u/2/c/NDUwOTk2NDQxODQz/m/NDUwOTk2NDQxODYw/details
#Q1-6
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize, sent_tokenize

text = open("New Text Document.txt").read()

print('Word tokenize', word_tokenize(text))
#print(sent_tokenize(text))

#lower case
print(text.lower())

#remove numbers

import re

def remove_number(text1) :
    text1 = re.sub(r'[0-9]', '', text1)
    return text1

text1 = "0eefe 8efe 8efe0902109308755"
print(remove_number(text1))

#removing punctuation

import re

def remove_punctuation(text1):
    text1 = re.sub(r'[.,?!$#[\]{}():;\'\-"]', '', text1)
    return text1
text1 = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 mor e days !"
print('Removing punctuation', remove_punctuation(text1))    

#removing white spaces

def remove_space(text1):
    text1 = re.sub(r'[ ]', '', text1)
    return text1
text1 = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !"
print('Removing white space', remove_space(text1))    

#number to words

import nltk
import inflect


from nltk.tokenize import word_tokenize
p = inflect.engine()

def convert(text):
    #tokenizing
    temp = word_tokenize(text)

    new_string = []
    
    for word in temp: 
     # if word is a digit, convert the digit 
     # to numbers and append into the new_string list 
     if word.isdigit(): 
         temp_str = p.number_to_words(word) 
         new_string.append(temp_str) 

     # append the word as it is 
     else: 
         new_string.append(word) 
    new_string = ' '.join(new_string)
    print(new_string)


text = "Hey 0, you look like 1"
convert(text)
