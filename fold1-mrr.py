import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

RESULTS_ROOT = "/project/results/paper2/europarl/fold1/"
engsentenceembedding = open(RESULTS_ROOT + "sen.en",'r', encoding='utf-8')
desentenceembedding = open(RESULTS_ROOT + 'sen.de','r', encoding='utf-8')

print("fold1-mrr.py is running.")
print("Processing sentence embedding files...")
engsent = []
desent = []
for line in engsentenceembedding:
    word = ''
    vectorlist = []
    for char in line:
        if char != ' ':
            word += char
        else:
            vectorlist.append(float(word))
            word = ''
    engsent.append(vectorlist)

for line in desentenceembedding:
    word = ''
    vectorlist = []
    for char in line:
        if char != ' ':
            word += char
        else:
            vectorlist.append(float(word))
            word = ''
    desent.append(vectorlist)

print("Compare eng sentence to all german sentence...")
engrrlist = []
for engline in engsent:
    cossimilarity = []
    for deline in desent:
        cossimilarity.append(cosine_similarity([engline],[deline]))
    actualline = cossimilarity[engsent.index(engline)]
    orderedcos = cossimilarity.sort(reverse = True)
    rank = cossimilarity.index(float(actualline)) + 1
    reciprocalrank = 1/rank
    engrrlist.append(reciprocalrank)
value = 0
for i in engrrlist:
    value += i 
engmrr = value / len(engrrlist)
print(engmrr)

print("Compare de sentence to all eng sentence...")
derrlist = []
for deline in desent:
    cossimilarity = []
    for engline in engsent:
        cossimilarity.append(cosine_similarity([engline],[deline]))
    actualline = cossimilarity[desent.index(deline)]
    orderedcos = cossimilarity.sort(reverse = True)
    rank = cossimilarity.index(float(actualline)) + 1
    reciprocalrank = 1/rank
    derrlist.append(reciprocalrank)
value2 = 0
for i in derrlist:
    value2 += i 
demrr = value2 / len(derrlist)
print(demrr)

print("Calculating overall mrr...")
mrr = (engmrr + demrr)/2
print(mrr)

with open(RESULTS_ROOT + 'mrr-fold1', 'w+', encoding='utf-8') as writeFile:
    writeFile.write("engmrr is " + str(engmrr))
    writeFile.write("demrr is " + str(demrr))
    writeFile.write("final mrr is " + str(mrr))

engsentenceembedding.close()
desentenceembedding.close()
print("fold1-mrr.py has completed.")