import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

RESULTS_ROOT = "/project/results/paper2/europarl/fold1/"
engsentenceembedding = open(RESULTS_ROOT + "sen.en",'r', encoding='utf-8')
desentenceembedding = open(RESULTS_ROOT + 'sen.de','r', encoding='utf-8')

print("fold1-acc.py is running.")
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
engtflist=[]
for engline in engsent:
    cossimilarity = []
    for deline in desent:
        cossimilarity.append(cosine_similarity([engline],[deline]))
    actualline = cossimilarity[engsent.index(engline)]
    orderedcos = cossimilarity.sort(reverse = True)
    rank = cossimilarity.index(float(actualline)) + 1
    if rank<11:
        engtflist.append(True)
    else:
        engtflist.append(False)    
truecount = engtflist.count(True)
engaccuracy = truecount/len(engtflist)
print(engaccuracy)

print("Compare de sentence to all english sentence...")
detflist=[]
for deline in desent:
    cossimilarity = []
    for engline in engsent:
        cossimilarity.append(cosine_similarity([engline],[deline]))
    actualline = cossimilarity[desent.index(deline)]
    orderedcos = cossimilarity.sort(reverse = True)
    rank = cossimilarity.index(float(actualline)) + 1
    if rank<11:
        detflist.append(True)
    else:
        detflist.append(False)    
truecount2 = detflist.count(True)
deaccuracy = truecount2/len(detflist)
print(deaccuracy)

print("Calculating overall acc...")
acc = (engaccuracy + deaccuracy)/2
print(acc)

with open(RESULTS_ROOT + "acc-fold1", 'w+', encoding="utf-8") as writeFile:
    writeFile.write("engacc is " + str(engaccuracy))
    writeFile.write("deacc is " + str(deaccuracy))
    writeFile.write("final acc is " + str(acc))

engsentenceembedding.close()
desentenceembedding.close()
print("fold1-acc.py has completed.")