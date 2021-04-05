#!/usr/bin/python3
# NOTE: Programme arguments
# DATA_NAME = input("What is the name: ") #datafilename (before.)
NUM_LANG = int(input("What is the number of languages that you want to make training files for: "))
ROOT = input("What is the root directory: ")  #folder with data file

# NOTE: THos file expects your 5 folds of data to be named test_N.LANG
# Where N is the nth fold of the data, and LANG is the language code
print("Starting:")
LANG_ARRAY = ("en", "de", "combined", "reversed")
testIter = ["test_1", "test_2", "test_3", "test_4", "test_5"]
for i in range(NUM_LANG):
    LANG = input("Enter language code: ")
    for k in range(5):
        print("Making " + str(k+1) + "th file for training")
        saveFile = open(ROOT + "/train_" + str(k+1) + "." + LANG , 'w+', encoding='utf-8')
        for j in testIter:
            if testIter.index(j) != k:
                print("Adding the " + j + "th line into the training file")
                tmp = ROOT + "/test_" + str(testIter.index(j)+1) + "." + LANG 
                with open(tmp, 'r', encoding='utf-8') as readFile:
                    for line in readFile:
                        saveFile.write(line)
            print("\n")
        saveFile.close()

