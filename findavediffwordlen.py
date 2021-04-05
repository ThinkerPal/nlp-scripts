from statistics import mean

RESULTS_ROOT = "/project/data/europarl/"
SOURCE_TEST = open(RESULTS_ROOT + "Europarlrev.de-en.de" , 'r', encoding='utf-8') 
TARGET_TEST = open(RESULTS_ROOT + "Europarlrev.de-en.en" , 'r', encoding='utf-8')

print("Starting to process source file...")
sourcelength = []
targetlength = []
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

print("Starting to process target file...")
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

print("Calculating length diff...")
lengthdiff = []
for i in range(len(sourcelength)):
    if sourcelength[i] > targetlength[i]:
        diff = sourcelength[i] - targetlength[i]
    elif targetlength[i] > sourcelength[i]:
        diff = targetlength[i] - sourcelength[i]
    else:
        diff = 0
    lengthdiff.append(diff)

avesentlength = mean(lengthdiff)
print(avesentlength)