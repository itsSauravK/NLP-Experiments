#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:08:19 2022

@author: sauravkumar
"""
#https://classroom.google.com/u/2/c/NDUwOTk2NDQxODQz/m/NDUwOTk2NDQxODYw/details
#Q7-9
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Removing stop words
def remove_stopWprds(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = []
    for word in word_tokens:
        if word not in stop_words:
            filtered_text.append(word)
        
    print(filtered_text)
    
text = 'This is a sample sentence and we are going to remove the stopwords from this'
remove_stopWprds(text)

#Removing stop word for marathi
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from cltk.stop.marathi.stops import STOP_LIST

def marathi_stop(text):
    word_tokens = word_tokenize(text) 
    filtered_text = [word for word in word_tokens if word not in STOP_LIST] 
    print('marathi',filtered_text)
example_text = "आपण खाली बसू या"
marathi_stop(example_text)


#Removing stop words in hindi
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from cltk.stop.classical_hindi.stops import STOPS_LIST

def hindi_stop(text):
    word_tokens = word_tokenize(text) 
    filtered_text = [word for word in word_tokens if word not in STOPS_LIST] 
    print('hindi',filtered_text)
example_text = "अमेरिका की तरह घर से पढ़ाई कर मिल जाता है सर्टिफिकेट, कॉलेज एडमिशन की फिक्र भी नहीं"
hindi_stop(example_text)



#Porter stemmer
import nltk
from nltk.stem import PorterStemmer 
stemmer = PorterStemmer()

def stem_words(text):
    word_tokens = word_tokenize(text)
    stems = []
    for word in word_tokens:
        stems.append(stemmer.stem(word))
       
    print ('Porter Stemmer: ',stems)
text = 'data science uses scientific methods algorithms and many types of processes'
stem_words(text)

#Lancester stemmer
import nltk
from nltk.stem import LancasterStemmer
stemmer = LancasterStemmer()

def Lanc_stem_words(text):
    word_tokenize(text)
    stems = []
    for word in word_tokenize(text):
        stems.append(stemmer.stem(word))
    print ('Lancestor :',stems)
text = 'data science uses scientific methods algorithms and many types of processes'
Lanc_stem_words(text)


#Lemmatization
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
#Lemmatize string
def lemmatize_word(text):
    word_tokens = word_tokenize(text)
    #provide part of speech
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in word_tokens]
    print('lemmatize: ', lemmas)
    
text = 'data science uses scientific methods algorithms and many types of processes'
lemmatize_word(text)

    