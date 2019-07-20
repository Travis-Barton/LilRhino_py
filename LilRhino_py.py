## LilRhino for Python 
import random

'''
Function for creating posotive or negative active labels.
doc:    List of documents to classify
k:      Number of items to label

return: A list of [[sentence 1, pos/neg], ..., [sentence k, pos/neg]]


NOTE:   Entering 0 is neutral or 'skip'. Those examples will NOT be labeled or included in 'return'.

EX:

test_sent = ['I\'m happy!', 'I\'m happy!', 'I\'m sad', 'I\'m sad', 'I\'m neutral', 'I\'m neutral', 'I\'m neutral']

temp = active_label(test_sent, 5)

print(temp)

'''
def active_label(docs, k):
    labeled = []
    index = random.sample(range(len(docs)), k)
    to_label = [[docs[i], i] for i in index]
    for item in to_label:
        print('pos = 1, neg = 2 or skip = 0 \n', item[0])
        choice = input(": ")
        choice_dict = {'1' : 'pos', '2' : 'neg'}
        if choice != '0':
            labeled.append([item[0], choice_dict[choice]])
    return(labeled)

