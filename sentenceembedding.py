# sentenceembedding.py
# # to obtain german sent embeddings ; rerun for english
wordembed = open('/project/results/paper2/Europarl/finalfull1/out.de' , 'r') #change file to 'lang' word embeddings
testdataset = open('','r')# open test data set file in 'lang'
sentenceembeddingfile = open('germansentenceembedding.txt','w') # open new file to contain sent embedding in each line

dict = {}
for i in wordembed:  #create dictionary
    word = ''
    embedding = ''
    for character in i:
        if character != ' ':
            word += character
        else:
            break
    print(word)
    
    for character in i:
        if character != "\n":
            embedding += character
        else:
            break
    vector = embedding.replace(word + ' ' , '')
    dict['word'] = 'vector' 

def extract(key) : #function to process value(fromkey:value pair) into list with floats
    string = dict.get(key)
    word2 = ''
    list = []
    for i in string: #if end of line no whitespace then nd to edit wordembededfile first(addwhitespace at end of each line)
        if i != ' ':
            word2 += i
        else:
            list.append(float(word2))
            word2 = ''
    return list

for line in testdataset: #extracting sentence embedding from test dataset
    word3 = ''
    wordlist = [] #list of words in 1 line
    wordembeddinglist = [] #nested array consist of word embedding of all words in a line separated in a list
    for char in line: #if end of line no whitespace then nd to edit testdatsetfile first(addwhitespace at end of each line)
        if char != ' ':
            word3 += char
        else:
            wordlist.append(word3)
            word3 = ''
    for i in range(len(wordlist)):
        wordembeddinglist.append(extract(wordlist[i]))
    sentembedding = []
  
    for dimension in range(len(wordembeddinglist[0])):    #no. of dimensions - 1 & assume number of dimensions for each word embedding is equal
        value = 0
        for word in range(len(wordlist)):
            value += wordembeddinglist[word][dimension]
        sentembedding.append(value)
           
    
    sentembeddingline = '' #write sentenceembedding into file
    for h in sentembedding:
        sentembeddingline = sentembeddingline + str(h) + ' '
    sentenceembeddingfile.write(sentembeddingline + '\n') #sentenceembeddingfile will hav every sentence embeddding (with 300 dimensions) per line ; ie 0.9999 0.5546 0.56446 0.5646...

#close all file
wordembed.close()
testdataset.close()
sentenceembeddingfile.close()

