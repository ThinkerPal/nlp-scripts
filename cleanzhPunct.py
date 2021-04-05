#!/usr/bin/python3
import io
import string
from zhon import hanzi as han
import random
from sklearn.model_selection import train_test_split

# NOTE: Programme arguments
DATA_NAME = input("What is the name: ") #datafilename (before.)
SOURCE_LANG = input("What is the Source Language: ") #langcode
TARGET_LANG = input("What is the Target Language: ")
ROOT = "/home/thinkerpal/Desktop/project/data/act-multiun" #folder with data file


FILE_BASE = ROOT + "/" + DATA_NAME + "." 
PUNC_RM_TABLE = str.maketrans(dict.fromkeys(string.punctuation))
ZH_PUNC_RM_TABLE = str.maketrans(dict.fromkeys(han.punctuation))

trg_og = open(FILE_BASE + TARGET_LANG, 'r', encoding='utf-8')

filterred_trg = []
print("removing from target language")
counter = 0
for line in trg_og:
    if counter % 1000000 == 0:
        print("Target Lines Filtered: ", counter)
    if line == "\n":
        continue
    line = line.strip()
    if line == "":
        continue
    elif line == "\n":
        continue
    elif line == "\n\r":
        continue
    if TARGET_LANG == 'zh':
        line = line.translate(ZH_PUNC_RM_TABLE)
       
        filterred_trg.append(line + " ")
    else:
        line = line.translate(PUNC_RM_TABLE)
        filterred_trg.append(line.lower() + " ")
    counter += 1
trg_og.close()
print("Sentences in trg lang: ", len(filterred_trg))
cleaned_punct = open(FILE_BASE + "punct." + TARGET_LANG, 'w+', encoding='utf-8')
for line in filterred_trg:
    cleaned_punct.write(line + "\n")