#!/usr/bin/python3

en = open('../europarl/results/test_5.en', 'r', encoding='utf-8')
de = open('../europarl/results/test_5.de', 'r', encoding='utf-8')
combinedFile = open('../europarl/results/test_5.reversed', 'w+', encoding='utf-8')

enList = []
deList = []

for i in en:
    i = i.strip()
    enList.append(i)

for i in de:
    i = i.strip()
    deList.append(i)

firstline = True
for i in range(len(enList)):
    if not firstline:
        combinedFile.write("\n")
    else: 
        firstline = False
    line = enList[i] + " ||| " + deList[i]
    combinedFile.write(line)
combinedFile.close()
en.close()
de.close()