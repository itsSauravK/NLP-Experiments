#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:31:54 2022

@author: sauravkumar
"""

from nltk.corpus import wordnet
print("Finding all the synonym set (SynSet) of a word for all possible POS tags" )
synsets = wordnet.synsets('dog') 
print(synsets)
print("Finding the synset if POS tag is known and number of senses") 
synset = wordnet.synset('dog.n.01')
print("Printing the definition(gloss) for the word 'dog'") 
print(synset.definition)
print("find the hypernym of a synset") 
dog = wordnet.synset('dog.n.01') 
print(dog.hypernyms())
print("find the hyponyms of a synset") 
print(dog.hyponyms())
print("Find commmon hypernyms between two words") 
dog = wordnet.synset('dog.n.01')
cat = wordnet.synset('cat.n.01')


 
print(dog.lowest_common_hypernyms(cat)) #Finding similarities between words
dog = wordnet.synset('dog.n.01') 
cat = wordnet.synset('cat.n.01') 
tree = wordnet.synset('tree.n.01')
print("Path similarity:Return a score denoting how similar two word senses are, based on the shortest path that connects the senses in the is-a (hypernym/hypnoym) taxonomy. The score is in the range 0 to 1")
print(wordnet.path_similarity(dog,cat)) 
print(wordnet.path_similarity(dog,tree))
print("Leacock-Chodorow Similarity: Return a score denoting how similar two word senses are, based on the shortest path that connects the senses (as above) and the maximum depth of the taxonomy in which the senses occur")
print(wordnet.lch_similarity(dog,cat)) 
print(wordnet.lch_similarity(dog,tree))
print("Wu-Palmer Similarity: Return a score denoting how similar two word senses are, based on the depth of the two senses in the taxonomy and that of their Least Common Subsumer (most specific ancestor node).")
print(wordnet.wup_similarity(dog,cat))
print(wordnet.wup_similarity(dog,tree))
