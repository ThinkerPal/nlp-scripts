from statistics import mean

RESULTS_ROOT = "/project/data/europarl/"
SOURCE_FILE = open(RESULTS_ROOT + "Europarlrev.de-en.de" , 'r', encoding='utf-8') 
TARGET_FILE = open(RESULTS_ROOT + "Europarlrev.de-en.en" , 'r', encoding='utf-8')

sourcelength = []
targetlength = []
print("Starting to process source file...")
for line in SOURCE_FILE:
    charlist = []
    for char in line:
        if char != ' ':
            charlist.append(char)
        else:
            continue
    sourcelength.append(len(charlist))

print("Starting to process target file...")
for line in TARGET_FILE:
    charlist = []
    for char in line:
        if char != ' ':
            charlist.append(char)
        else:
            continue
    targetlength.append(len(charlist))

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