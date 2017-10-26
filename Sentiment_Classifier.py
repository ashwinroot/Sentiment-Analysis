import re
import getInput
from nltk.corpus import stopwords
from collections import defaultdict
import random
import nltk
from itertools import islice
stopset = list(set(stopwords.words('english')))


'''
initialising global parameters
'''
total_dictionary, positive_dicitonary, negative_dictionary,no_positive, no_negative = defaultdict(),defaultdict(),defaultdict(),0,0

def word_feats(words):
    return dict([(word, True) for word in words.split() if word not in stopset])

'''
my implementation of Navies Bayes Classifier
'''

def NB_Classifier(sentence):
    #get the word list for the sentence to perform NB
    word_list = getInput.remove_stop_words_stem(sentence)


    #initialize the probabilities
    positive_prob = 1
    negative_prob = 1


    #Finding the positve Probability
    for word in word_list:
        if word in total_dictionary:
            positive_prob *= ((total_dictionary[word]['POS'] if 'POS' in total_dictionary[word] else 1 )/ no_positive)
        else:
            positive_prob *= 1/ no_positive
    positive_prob *= (len(positive_dicitonary) / (len(positive_dicitonary) + len(negative_dictionary)))

    #finding the negative probability
    for word in word_list:
        if word in total_dictionary:
            negative_prob *= ((total_dictionary[word]['NEG'] if 'NEG' in total_dictionary[word] else 1 )/ no_negative)
        else:
            negative_prob *= 1/ no_negative
    negative_prob *= (len(negative_dictionary) / (len(positive_dicitonary) + len(negative_dictionary)))

    if positive_prob>=negative_prob:
        return 'POS'
    else:
        return 'NEG'

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


'''
implemented to compare with my model
'''
def NLTK_NB(sentence):
    if 'total_dictionary' not in locals():
        total_dictionary,positive_dicitonary,negative_dictionary,no_positive,no_negative = getInput.get_complete_dictionary()
    labelled = list()
    #constructing labelled data
    pos_feats = [(word_feats(positive_dicitonary[f]), 'positive') for f in positive_dicitonary]
    neg_feats = [(word_feats(negative_dictionary[f]), 'negative') for f in negative_dictionary]
    labelled = pos_feats + neg_feats
    classifier = nltk.NaiveBayesClassifier.train(labelled)
    return classifier.classify(word_feats(sentence))

'''
initializing the variables
'''

def train():
    global total_dictionary
    global  positive_dicitonary
    global negative_dictionary
    global no_positive
    global no_negative
    total_dictionary, positive_dicitonary, negative_dictionary, no_positive, no_negative=getInput.get_complete_dictionary_without_stopwords()



