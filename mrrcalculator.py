import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

engsentenceembedding = open('','r')
desentenceembedding = open('','r')

# process sentence embedding file
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

#compare eng sentence to all german sentence
rrlist = []
for engline in engsent:
    cossimilarity = []
    for deline in desent:
        cossimilarity.append(cosine_similarity([engline],[deline]))
    actualline = cossimilarity[engsent.index(engline)]
    orderedcos = cossimilarity.sort(reverse = True)
    rank = cossimilarity.index(int(actualline))
    reciprocalrank = 1/rank
    rrlist.append(reciprocalrank)

value = 0
for i in rrlist:
    value += i 
mrr = value / len(rrlist)
print(mrr)

with open('/project/results/paper2/mrrResult', 'w+', encoding='utf-8') as writeFile:
    writeFile.write(mrr)