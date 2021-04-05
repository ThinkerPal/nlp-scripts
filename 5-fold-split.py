#!/usr/bin/python3
import io
import string
from zhon import hanzi as han
import os
import random
import threading
from sklearn.model_selection import train_test_split

# NOTE: Programme arguments
DATA_NAME = input("What is the name: ") #datafilename (before.)
SOURCE_LANG = input("What is the Source Language: ") #langcode
TARGET_LANG = input("What is the Target Language: ")
ROOT = input("What is the root directory: ")  #folder with data file


FILE_BASE = ROOT + "/" + DATA_NAME + "." + SOURCE_LANG + "-" + TARGET_LANG + "." 
PUNC_RM_TABLE = str.maketrans(dict.fromkeys(string.punctuation))
ZH_PUNC_RM_TABLE = str.maketrans(dict.fromkeys(han.punctuation))

src_og = open(FILE_BASE + SOURCE_LANG, 'r', encoding='utf-8')
trg_og = open(FILE_BASE + TARGET_LANG, 'r', encoding='utf-8')
test1_combined = open(ROOT + '/results/test_1.combined', 'w+', encoding='utf-8')
test1_reversed = open(ROOT + '/results/test_1.reversed', 'w+', encoding='utf-8')
test1_src = open(ROOT + '/results/test_1.' + SOURCE_LANG, 'w+', encoding='utf-8')
test1_trg = open(ROOT + '/results/test_1.' + TARGET_LANG, 'w+', encoding='utf-8')
test2_combined = open(ROOT + '/results/test_2.combined', 'w+', encoding='utf-8')
test2_reversed = open(ROOT + '/results/test_2.reversed', 'w+', encoding='utf-8')
test2_src = open(ROOT + '/results/test_2.' + SOURCE_LANG, 'w+', encoding='utf-8')
test2_trg = open(ROOT + '/results/test_2.' + TARGET_LANG, 'w+', encoding='utf-8')
test3_combined = open(ROOT + '/results/test_3.combined', 'w+', encoding='utf-8')
test3_reversed = open(ROOT + '/results/test_3.reversed', 'w+', encoding='utf-8')
test3_src = open(ROOT + '/results/test_3.' + SOURCE_LANG, 'w+', encoding='utf-8')
test3_trg = open(ROOT + '/results/test_3.' + TARGET_LANG, 'w+', encoding='utf-8')
test4_combined = open(ROOT + '/results/test_4.combined', 'w+', encoding='utf-8')
test4_reversed = open(ROOT + '/results/test_4.reversed', 'w+', encoding='utf-8')
test4_src = open(ROOT + '/results/test_4.' + SOURCE_LANG, 'w+', encoding='utf-8')
test4_trg = open(ROOT + '/results/test_4.' + TARGET_LANG, 'w+', encoding='utf-8')
test5_combined = open(ROOT + '/results/test_5.combined', 'w+', encoding='utf-8')
test5_reversed = open(ROOT + '/results/test_5.reversed', 'w+', encoding='utf-8')
test5_src = open(ROOT + '/results/test_5.' + SOURCE_LANG, 'w+', encoding='utf-8')
test5_trg = open(ROOT + '/results/test_5.' + TARGET_LANG, 'w+', encoding='utf-8')
print("All necessary files opened")
filterred_src = []
filterred_trg = []
#no_punctuation = sentence.translate(PUNC_RM_TABLE)

# NOTE: Removing punctuations, blank lines and making a list from the file
print("Removing punctuations, blank lines and making a list from the file")
counter = 0
for line in src_og:
    if counter % 1000000 == 0:
        print("Lines filtered: ", counter)
    if line == "\n":
        continue
    line = line.strip()
    if line == "":
        continue
    elif line == "\n":
        continue
    elif line == "\n\r":
        continue
    if SOURCE_LANG == 'zh':
        line = line.translate(ZH_PUNC_RM_TABLE)
        filterred_src.append(line + " ")
    else:
        line = line.translate(PUNC_RM_TABLE)
        filterred_src.append(line.lower() + " ")
    counter += 1
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
src_og.close()
trg_og.close()
print("Sentences in src lang: ", len(filterred_src))
print("Sentences in trg lang: ", len(filterred_trg))

# NOTE: Filtering out sentences with less than 10 words to improve data cleaniless
print("Filtering out sentences with less than 30 characters to improve data cleaniless")
SENTENCE_THRESHOLD = 30
if SOURCE_LANG == 'zh': #Overrides for default sentence length
    SENTENCE_THRESHOLD = 7
counter = 0
changed = 0
for i in range(len(filterred_src)):
    if counter % 50000 == 0:
        print("Source dammed Lines Filtered: ", counter)
    if changed % 50 == 0:
        print("Number of lines changed:", changed)
    if len(filterred_src[i]) < SENTENCE_THRESHOLD:
        changed += 1
        filterred_trg.pop(i)
        filterred_src.pop(i)
    counter += 1

if TARGET_LANG == 'zh': #Overrides for default sentence length
    SENTENCE_THRESHOLD = 7
else:
    SENTENCE_THRESHOLD = 30
counter = 0
changed = 0
print("filterring target")
for line in filterred_trg:
    if counter % 50000 == 0:
        print("Target dammed Lines Filtered: ", counter)
    if changed % 50 == 0:
        print("Target lines changed:", changed)
    if len(line) < SENTENCE_THRESHOLD:
        # print(line)
        changed += 1
        filterred_src.pop(filterred_trg.index(line))
        filterred_trg.remove(line)
    counter += 1
        
counter = 0
changed = 0
# NOTE: Splitting of data occurs here
print("Splitting Data")
print("Sentences in src lang: " + str(len(filterred_src)))
print("Sentences in trg lang: " + str(len(filterred_trg)))
if len(filterred_src) != len(filterred_trg):
    Continue_state = input("ERROR OCCURRED: Lines in Source and Target Languages are different. Continue? (Y/N)")
    if Continue_state != 'Y':
        print("Exiting...")
        os._exit(0)
if len(filterred_src) % 5 != 0:
    for i in range(len(filterred_src) % 5):
        toRemove = random.choice(filterred_src)
        toRemoveIndex = filterred_src.index(toRemove)
        filterred_src.pop(toRemoveIndex)
        filterred_trg.pop(toRemoveIndex)

print("Starting split")
src_rest, srcTest1, trg_rest, trgTest1 = train_test_split(filterred_src, filterred_trg, test_size = 0.2, random_state = 42)
print("Spliting quater done")
srcRestHalf, srcRest2, trgRestHalf, trgRest2 = train_test_split(src_rest, trg_rest, test_size = 0.5, random_state = 42)
print("Splitting half done")
srcTest2, srcTest3, trgTest2, trgTest3 = train_test_split(srcRestHalf, trgRestHalf, test_size = 0.5, random_state = 42)
print("I would like my split medium well")
srcTest4, srcTest5, trgTest4, trgTest5 = train_test_split(srcRest2, trgRest2, test_size = 0.5, random_state = 42)

# Saving files
print("Saving Data")
firstLine = True
for i in srcTest1:
    if not firstLine:
        test1_src.write("\n")
    else:
        firstLine = False
    test1_src.write(i)
firstLine = True
for i in srcTest2:
    if not firstLine:
        test2_src.write("\n")
    else:
        firstLine = False
    test2_src.write(i)
print("2 src done")
firstLine = True
for i in srcTest3:
    if not firstLine:
        test3_src.write("\n")
    else:
        firstLine = False
    test3_src.write(i)
firstLine = True
for i in srcTest4:
    if not firstLine:
        test4_src.write("\n")
    else:
        firstLine = False
    test4_src.write(i)
print("Almost done with sorce data")
firstLine = True
for i in srcTest5:
    if not firstLine:
        test5_src.write("\n")
    else:
        firstLine = False
    test5_src.write(i)
firstLine = True
print("Saving Target Data")
# NOTE: ITS STUFF OF TARGET WOOO
for i in trgTest1:
    if not firstLine:
        test1_trg.write("\n")
    else:
        firstLine = False
    test1_trg.write(i)
print("1 done")
firstLine = True
for i in trgTest2:
    if not firstLine:
        test2_trg.write("\n")
    else:
        firstLine = False
    test2_trg.write(i)
print("2 done")
firstLine = True
for i in trgTest3:
    if not firstLine:
        test3_trg.write("\n")
    else:
        firstLine = False
    test3_trg.write(i)
firstLine = True
for i in trgTest4:
    if not firstLine:
        test4_trg.write("\n")
    else:
        firstLine = False
    test4_trg.write(i)
print("almost done with target data")
firstLine = True
for i in trgTest5:
    if not firstLine:
        test5_trg.write("\n")
    else:
        firstLine = False
    test5_trg.write(i)
firstLine = True
# NOTE: COMBINED FILES
print("saving combined src-trg files")
for i in range(len(srcTest1)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = srcTest1[i] + ' ||| ' + trgTest1[i]
    if not firstLine:
        test1_combined.write("\n")
    else: 
        firstLine = False
    test1_combined.write(d)
firstLine = True
for i in range(len(srcTest2)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = srcTest2[i] + ' ||| ' + trgTest2[i]
    if not firstLine:
        test2_combined.write("\n")
    else:
        firstLine = False
    test2_combined.write(d)
firstLine = True
print("Medium rare combined source")
for i in range(len(srcTest3)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = srcTest3[i] + ' ||| ' + trgTest3[i]
    if not firstLine:
        test3_combined.write("\n")
    else:
        firstLine = False
    test3_combined.write(d)
firstLine = True
for i in range(len(srcTest4)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = srcTest4[i] + ' ||| ' + trgTest4[i]
    if not firstLine:
        test4_combined.write("\n")
    else:
        firstLine = False
    test4_combined.write(d)
firstLine = True
for i in range(len(srcTest5)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = srcTest5[i] + ' ||| ' + trgTest5[i]
    if not firstLine:
        test5_combined.write("\n")
    else:
        firstLine = False
    test5_combined.write(d)
firstLine = True
# NOTE: trg-src reversed files
print("Saving Reversed Trg-Src combined files")
for i in range(len(srcTest1)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = trgTest1[i] + ' ||| ' + srcTest1[i]
    if not firstLine:
        test1_reversed.write("\n")
    else:
        firstLine = False
    test1_reversed.write(d)
firstLine = True
for i in range(len(srcTest2)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = trgTest2[i] + ' ||| ' + srcTest2[i]
    if not firstLine:
        test2_reversed.write("\n")
    else:
        firstLine = False
    test2_reversed.write(d)
firstLine = True
for i in range(len(srcTest3)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = trgTest3[i] + ' ||| ' + srcTest3[i]
    if not firstLine:
        test3_reversed.write("\n")
    else:
        firstLine = False
    test3_reversed.write(d)
firstLine = True
print("No ruler vector additional - I am high at 3am")
for i in range(len(srcTest4)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    d = trgTest4[i] + ' ||| ' + srcTest4[i]
    if not firstLine:
        test4_reversed.write("\n")
    else:
        firstLine = False
    test4_reversed.write(d)
firstLine = True
for i in range(len(srcTest5)):
    # if srcTest1[i].strip == "":
    #     continue 
    # else:
    firstLine = False
    if not firstLine:
        test5_reversed.write("\n")
    else:
        d = trgTest5[i] + ' ||| ' + srcTest5[i]
    test5_reversed.write(d)
        
# Closing files
test1_src.close()
test1_trg.close()
test1_combined.close()
test1_reversed.close()
test2_src.close()
test2_trg.close()
test2_combined.close()
test2_reversed.close()
test3_src.close()
test3_trg.close()
test3_combined.close()
test3_reversed.close()
test4_src.close()
test4_trg.close()
test4_combined.close()
test4_reversed.close()
test5_src.close()
test5_trg.close()
test5_combined.close()
test5_reversed.close()