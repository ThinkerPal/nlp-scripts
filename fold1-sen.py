#!/usr/bin/python3
# sentenceembedding.py
import os

RESULTS_ROOT = "/project/results/paper2/europarl/fold1/"
DE_word = open(RESULTS_ROOT + "out.de" , 'r', encoding='utf-8') #change file to 'lang' word embeddings
DE_test = open('/project/data/europarl/results/test_1.de','r', encoding='utf-8')# open test data set file in 'lang'
DE_Sent = open(RESULTS_ROOT + "sen.de",'w+', encoding='utf-8') # open new file to contain sent embedding in each line
EN_word = open(RESULTS_ROOT + "out.en", 'r', encoding='utf-8')
EN_test = open('/project/data/europarl/results/test_1.en','r', encoding='utf-8')# open test data set file in 'lang'
EN_Sent = open(RESULTS_ROOT + "sen.en", 'w+', encoding='utf-8')

print("Running fold1-sen.py")
def total(wordembed, testdataset, sentenceembeddingfile):
    print("Creating dictonary...")
    dict = {}
    for i in wordembed:  #create dictionary
        word = ''
        embedding = ''
        for character in i:
            if character != ' ':
                word += character           
            else:
                break
        
        for character in i:
            if character != "\n":
                embedding += character
            else:
                break
        vector = embedding.replace(word + ' ' , '' , 1)
        dict[word] = vector

    print("Creating extract functon...")
    def extract(key) : #function to process value(fromkey:value pair) into list with floats
        string = dict.get(key)
        word2 = ''
        list = []
        if not string == None:
            for i in string: #if end of line no whitespace then nd to edit wordembededfile first(addwhitespace at end of each line)
                if i != ' ':
                    word2 += i
                else:
                    list.append(float(word2))
                    word2 = ''
        return list

    print("Extracting sentence embedding from test dataset...")
    for line in testdataset: #extracting sentence embedding from test dataset
        word3 = ''
        wordlist = [] #list of words in 1 line
        wordembeddinglist = [] #nested array consist of word embedding of all words in a line separated in a list
        firstchar = True
        for char in line: #if end of line no whitespace then nd to edit testdatsetfile first(addwhitespace at end of each line)
            if firstchar and char == ' ':
                firstchar = False
                continue
            elif char != ' ':
                word3 += char
            else:
                wordlist.append(word3)
                word3 = ''
            firstchar = False
        for i in range(len(wordlist)):
            wordembeddinglist.append(extract(wordlist[i]))
        
        sentembedding = []
        for dimension in range(300):    #no. of dimensions - 1 & assume number of dimensions for each word embedding is equal
            value = 0
            for word in range(len(wordlist)):
                if not wordembeddinglist[word] == []:
                    value += wordembeddinglist[word][dimension]
                else:
                    continue
            sentembedding.append(round(value, 6))
            
        
        sentembeddingline = '' #write sentenceembedding into file
        for h in sentembedding:
            sentembeddingline = sentembeddingline + str(h) + ' '
        sentenceembeddingfile.write(sentembeddingline + '\n') #sentenceembeddingfile will hav every sentence embeddding (with 300 dimensions) per line ; ie 0.9999 0.5546 0.56446 0.5646...

    wordembed.close()
    testdataset.close()
    sentenceembeddingfile.close()

print("Processing german")
total(DE_word, DE_test, DE_Sent)
print("Processing english")
total(EN_word, EN_test, EN_Sent)


print("fold1-sen.py has completed")

#os.system('python3 ./fold1-mrr.py')
#os.system('python3 ./fold1-acc.py')
