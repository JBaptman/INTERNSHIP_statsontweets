import nltk
import csv
import sys
import re
import time
import json
from string import punctuation
from collections import Counter
from nltk.book import *


######################################################################
#FUNCTIONS THAT REMOVE UNWANTED TEXT
######################################################################

def del_url(txt):
    pattern_url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.search(pattern_url, txt):
        return ' '.join(re.sub(pattern_url,'', txt).split())
    return txt

def del_mentions(txt):
    pattern_mentions = '(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)'
    if re.search(pattern_mentions, txt):
        return ' '.join(re.sub(pattern_mentions,'', txt).split())
    return txt

def del_hashtag(txt):
    pattern_hashtag = '#(\w+)'
    if re.search(pattern_hashtag, txt):
        return ' '.join(re.sub(pattern_hashtag,'', txt).split())
    return txt

def del_punctuation(txt):
    return ''.join(c for c in txt if c not in punctuation)

def del_all(txt):
    return del_hashtag(del_punctuation(del_mentions(del_url(txt))))


######################################################################
#FUNCTION THAT IDENTIFIES "AUTOMATIC TWEETS" FROM YOUTUBE", WHEN YOU LIKED A VIDEO
######################################################################
#Here are the 3 sentences that are tweeted, in English, in French and in German
#Just change the string in the function to remove the tweets you want

#"I liked a @YouTube video"
#"J'aime une vidéo @YouTube"
#"Ich habe ein @YouTube-Video"

def find_YTTweets(tweet):
    if "I liked a @YouTube video" in tweet:
        return False
    return True
    


######################################################################
#F#FUNCTIONS THAT COUNTS ENTTIES IN THE TWEETS
######################################################################

def nb_chars(tab):
    nbc = 0
    for tweet in tab:
        nbc += len(tweet)
        
    print("There are ", nbc, " characters")
    print("#######################################################")
    return nbc


def nb_words(tab):
    nbw = 0
    for tweet in tab:
        tmp = nltk.word_tokenize(tweet)
        nbw += len(tmp)

    print("There are ", nbw, " words")
    print("#######################################################")
    return nbw


def nb_wordset(tab):
    nbws = 0
    for tweet in tab:
        tmp = nltk.word_tokenize(tweet)
        nbws += len(set(tmp))

    print("There are ", nbws, " different words")
    print("#######################################################")
    return nbws


def lexical_diversity(tab):
    return nb_wordset(tab)/nb_words(tab)


def nb_nouns(tab):
    nbn = 0
    for tweet in tab:
        tmp = nltk.word_tokenize(tweet)
        for word, tag in nltk.pos_tag(tmp):
            if tag == 'NN':
                nbn += 1
                
    print("There are ", nbn, " nouns")
    print("#######################################################")
    return nbn


def nb_verbs(tab):
    nbv = 0
    for tweet in tab:
        tmp = nltk.word_tokenize(tweet)
        for word, tag in nltk.pos_tag(tmp):
            if 'VB' in tag:
                nbv += 1

    print("There are ", nbv, " verbs")
    print("#######################################################")
    return nbv



def nb_namedEntities(tab):
    namedEntArray = []
    nbne = 0
    for tweet in tab:
        tokenized = nltk.word_tokenize(tweet)
        tagged = nltk.pos_tag(tokenized)

        namedEnt = nltk.ne_chunk(tagged, binary=True)

        entities = re.findall(r'NE\s(.*?)/',str(namedEnt))
        descriptives = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'', str(tagged))
        nbne += len(entities)

    print("There are ", nbne, " named entities")
    print("#######################################################")
    return nbne



def most_common_words(tab, i):
    tmp = ' '.join(str(e) for e in tab)
    tmp2 = nltk.word_tokenize(tmp)
    mcw = FreqDist(tmp2)
    print("The ", i, " most common words are : ")
    print(mcw.most_common(i))
    print("#######################################################")
    return mcw

        

    
