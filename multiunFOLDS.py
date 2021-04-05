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
ROOT = "/home/thinkerpal/Desktop/project/data/act-multiun" #folder with data file


FILE_BASE = ROOT + "/" + DATA_NAME + "." 
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

# NOTE: Removing punctuations, blank lines and making a list from the file
print("Removing punctuations, blank lines and making a list from the file")
for line in src_og:
    line = line.strip()
    filterred_src.append(line.lower() + " ")

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

# 
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




a=0
# Saving files
print("Saving Data")
a=0
# NOTE: ITS STUFF OF TARGET WOOO
print(len(trgTest1))
b=len(trgTest1)
for i in range(b-a):
    # print(i)
    if i >= b-a:
        break
    elif trgTest1[i] == " " or trgTest1[i] == "":
        trgTest1.pop(i)
        srcTest1.pop(i)
        a+=1
    test1_trg.write(trgTest1[i]+ "\n")
print("1 done")
firstLine = True
a=0
b=len(trgTest2)
for i in range(b-a):
    if i>=b-a:
        break
    elif trgTest2[i] == " " or trgTest2[i] == "":
        trgTest2.pop(i)
        srcTest2.pop(i)
        a+=1
    test2_trg.write(trgTest2[i]+ "\n")
print("2 done")
firstLine = True
a=0
b=len(trgTest3)
for i in range(b-a):
    if i>=b-a:
        break
    elif trgTest3[i] == " " or trgTest3[i] == "":
        trgTest3.pop(i)
        srcTest3.pop(i)
        a+=1
    test3_trg.write(trgTest3[i]+ "\n")
firstLine = True
a=0
b=len(trgTest4)
for i in range(b-a):
    if i>=b-a:
        break
    elif trgTest4[i] == " " or trgTest4[i] == "":
        trgTest4.pop(i)
        srcTest4.pop(i)
        a+=1
    test4_trg.write(trgTest4[i]+ "\n")
print("almost done with target data")
firstLine = True
a=0
b=len(trgTest5)
for i in range(b-a):
    if i>=b-a:
        break
    elif trgTest5[i] == " " or trgTest5[i] == "":
        trgTest5.pop(i)
        srcTest5.pop(i)
        a+=1
    test5_trg.write(trgTest5[i]+ "\n")
for i in range(len(srcTest1)-a):
    if srcTest1[i] == " " or srcTest1[i] == "":
        srcTest1.pop(i)
        trgTest1.pop(i)
        a+=1
    test1_src.write(srcTest1[i] + "\n")
a=0
for i in range(len(srcTest2)-a):
    if srcTest2[i] == " " or srcTest2[i] == "":
        srcTest2.pop(i)
        trgTest2.pop(i)
        a+=1
    test2_src.write(srcTest2[i]+ "\n")
print("2 src done")
a=0
firstLine = True
for i in range(len(srcTest3)-a):
    if srcTest3[i] == " " or srcTest3[i] == "":
        srcTest3.pop(i)
        trgTest3.pop(i)
        a+=1
    test3_src.write(srcTest3[i]+ "\n")
a=0
for i in range(len(srcTest4)-a):
    if srcTest4[i] == " " or srcTest4[i] == "":
        srcTest4.pop(i)
        trgTest4.pop(i)
        a+=1
    test4_src.write(srcTest4[i]+ "\n")
a=0
print("Almost done with sorce data")
for i in range(len(srcTest5)-a):
    if srcTest5[i] == " " or srcTest5[i] == "":
        srcTest5.pop(i)
        trgTest5.pop(i)
        a+=1
    test5_src.write(srcTest5[i]+ "\n")
print("Saving Target Data")
a=0
firstLine = True
# NOTE: COMBINED FILES
firstLine = True
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