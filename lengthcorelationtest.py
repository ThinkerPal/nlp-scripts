import numpy as np

RESULTS_ROOT = "/project/data/europarl/"
SOURCE_TEST = open(RESULTS_ROOT + "Europarlrev.de-en.de" , 'r', encoding='utf-8')
TARGET_TEST = open(RESULTS_ROOT + "Europarlrev.de-en.en" , 'r', encoding='utf-8')

def total(mode):    
    sourcelength = []
    targetlength = []
    if mode == "word":
        SOURCE_TEST.seek(0)
        TARGET_TEST.seek(0)
        for line in SOURCE_TEST:
            wordlist = []
            word = ''
            for char in line:
                if char != ' ':
                    word += char
                else:
                    wordlist.append(word)
                    word = ''
            sourcelength.append(len(wordlist))

        for line in TARGET_TEST:
            wordlist = []
            word = ''
            for char in line:
                if char != ' ':
                    word += char
                else:
                    wordlist.append(word)
                    word = ''
            targetlength.append(len(wordlist))

        corrcoeff = np.corrcoef(sourcelength,targetlength)
        print(corrcoeff)
        print(corrcoeff[0][1])

    elif mode == "char":
        SOURCE_TEST.seek(0)
        TARGET_TEST.seek(0)
        for line in SOURCE_TEST:
            charlist = []
            for char in line:
                if char != ' ':
                    charlist.append(char)
                else:
                    continue
            sourcelength.append(len(charlist))

        for line in TARGET_TEST:
            charlist = []
            for char in line:
                if char != ' ':
                    charlist.append(char)
                else:
                    continue
            targetlength.append(len(charlist))

        corrcoeff2 = np.corrcoef(sourcelength,targetlength)
        print(corrcoeff2)
        print(corrcoeff2[0][1])

    else:
        print("ERROR")

total( mode = 'word' )
total( mode = 'char' )
