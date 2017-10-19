import re
from collections import defaultdict
import nltk
from nltk.corpus import stopwords

def read_file(filename,dictator):
    fp = open(filename)
    data = fp.read()
    #sep_sentence = tokenizer.tokenize(data)
    data = re.split(r'[\n]+', data) # group spliting
    for reviews in data:
        if reviews=='':
            continue
        id , review = re.split(r'[\t]+',reviews)
        dictator[id] =review
    return dictator

def get_complete_dictionary():
    positive_dict = {}
    negative_dict = {}
    positive_dict = read_file("Dataset/hotelPosT-train.txt",positive_dict)
    negative_dict = read_file("Dataset/hotelNegT-train.txt",negative_dict)
    positive_words = 0
    negative_words = 0
    common_dict = defaultdict(dict)

    for id in positive_dict:
        sentence = positive_dict[id]
        word_list = re.findall(r"[\w']+|[.,!?;]", sentence)
        for word in word_list:
            positive_words+=1
            if word not in common_dict:
                common_dict[word]['POS'] = 1
            else:
                common_dict[word]['POS'] +=1
    for id in negative_dict:
        sentence = negative_dict[id]
        word_list = re.findall(r"[\w']+|[.,!?;]", sentence)
        for word in word_list:
            negative_words+=1
            if word not in common_dict:
                common_dict[word]['NEG'] = 1
            elif 'NEG' not in common_dict[word]:
                common_dict[word]['NEG'] = 1
            else:
                common_dict[word]['NEG'] +=1
    return common_dict,positive_dict,negative_dict,positive_words,negative_words

def get_complete_dictionary_without_stopwords():
    positive_dict = {}
    negative_dict = {}
    positive_dict = read_file("Dataset/hotelPosT-train.txt",positive_dict)
    negative_dict = read_file("Dataset/hotelNegT-train.txt",negative_dict)
    positive_words = 0
    negative_words = 0
    common_dict = defaultdict(dict)

    for id in positive_dict:
        sentence = positive_dict[id]
        word_list = remove_stop_words(sentence)
        # word_list = re.findall(r"[\w']+|[.,!?;]", sentence)
        for word in word_list:
            positive_words+=1
            if word not in common_dict:
                common_dict[word]['POS'] = 1
            else:
                common_dict[word]['POS'] +=1
    for id in negative_dict:
        sentence = negative_dict[id]
        word_list = remove_stop_words(sentence)
        # word_list = re.findall(r"[\w']+|[.,!?;]", sentence)
        for word in word_list:
            negative_words+=1
            if word not in common_dict:
                common_dict[word]['NEG'] = 1
            elif 'NEG' not in common_dict[word]:
                common_dict[word]['NEG'] = 1
            else:
                common_dict[word]['NEG'] +=1
    return common_dict,positive_dict,negative_dict,positive_words,negative_words


def remove_stop_words(sentence):
    return_list =[]
    word_list = re.findall(r"[\w']+|[.,!?;]", sentence)
    for word in word_list:
        if word not in set(stopwords.words('english')):
            return_list.append(word)
    return return_list
