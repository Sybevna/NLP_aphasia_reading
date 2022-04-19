# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:24:08 2022

@author: scro4369
# """
# import nltk
# nltk.download('wordnet')
# nltk.download('punkt')
# from nltk.stem import WordNetLemmatizer 
# from nltk import word_tokenize, pos_tag
# # Init the Wordnet Lemmatizer
# lemmatizer = WordNetLemmatizer()
# stopwords = nltk.corpus.stopwords.words("english")
# from nltk.stem import PorterStemmer

# from collections import defaultdict
# from nltk.corpus import wordnet as wn
# from nltk.stem.wordnet import WordNetLemmatizer
# from nltk import word_tokenize, pos_tag
# from collections import defaultdict
# tag_map = defaultdict(lambda : wn.NOUN)
# tag_map['J'] = wn.ADJ
# tag_map['V'] = wn.VERB
# tag_map['R'] = wn.ADV
# #%% Read file
# text = []

# f= open("Oliver_twist.txt","r",encoding='utf-8')
# text = f.read()
            
# sentences = nltk.tokenize.sent_tokenize(text)

# ps = PorterStemmer()
# for sentence in sentences:
#     word_list = nltk.word_tokenize(sentence)
    
#     lemmatized_output = ' '.join([lemmatizer.lemmatize(w, tag_map[tag[0]]) for w, tag in pos_tag(word_list)])
#     text2.append(lemmatized_output)

import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict
from nltk.corpus import stopwords
tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV
f= open("Oliver_twist.txt","r",encoding='utf-8')
text = f.read()
text_lemma = []   
text_lemm_stpwrds = []     
sentences = nltk.tokenize.sent_tokenize(text)
lemma_function = WordNetLemmatizer()
#ps = PorterStemmer()
for sentence in sentences:
    tokens = word_tokenize(sentence)
    #for token, tag in pos_tag(tokens):
    #lemma = lemma_function.lemmatize(token, tag_map[tag[0]])
    lemma = ' '.join([lemma_function.lemmatize(token, tag_map[tag[0]]) for token, tag in pos_tag(tokens) ])
    #lemma_stpwrds = ' '.join([lemma_function.lemmatize(token, tag_map[tag[0]]) for token, tag in pos_tag(tokens) if token not in stopwords.words('english')])
    text_lemma.append(lemma)
    #text_lemm_stpwrds.append(lemma_stpwrds)
print("I'm done")

with open('text_lemmatized.txt', 'w',encoding='utf-8') as g:
    for text in text_lemma:
        g.write("%s\n" % text)