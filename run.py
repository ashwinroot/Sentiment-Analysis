import re

import getInput


def NB_Classifier(sentence):
    total_dictionary,positive_dicitonary,negative_dictionary,no_positive,no_negative = getInput.get_complete_dictionary_without_stopwords()

    word_list = re.findall(r"[\w']+|[.,!?;]", sentence)

    positive_prob = 1
    negative_prob = 1

    #Finding the positve Probability
    for word in word_list:
        positive_prob *= ((total_dictionary[word]['POS'] if 'POS' in total_dictionary[word] else 1 )/ no_positive)
        # print(word , '->' ,(total_dictionary[word]['POS'] / no_positive) )
    positive_prob *= (len(positive_dicitonary) / len(positive_dicitonary) + len(negative_dictionary))

    for word in word_list:
        negative_prob *= ((total_dictionary[word]['NEG'] if 'NEG' in total_dictionary[word] else 1 )/ no_negative)
        # negative_prob *= (total_dictionary[word]['NEG'] / no_negative)
        # print(word , '->' ,(total_dictionary[word]['NEG'] / no_negative))
    negative_prob *= (len(negative_dictionary) / len(positive_dicitonary) + len(negative_dictionary))

    if positive_prob>=negative_prob:
        return 'Positive',positive_prob*100/(positive_prob+negative_prob)
    else:
        return 'Negative',negative_prob*100/(positive_prob+negative_prob)
