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
tflist=[]
for engline in engsent:
    cossimilarity = []
    for deline in desent:
        cossimilarity.append(cosine_similarity([engline],[deline]))
    actualline = cossimilarity[engline.index(engsent)]
    orderedcos = cossimilarity.sort(reverse = True)
    rank = cossimilarity.index(int(actualline))
    if rank<11:
        tflist.append(True)
    else:
        tflist.append(False)    
truecount = tflist.count(True)
accuracy = truecount/len(engsent)
print(accuracy)
with open('/project/result/paper2/accuracyResults', 'w+', encoding="utf-8") as writeFile:
    writeFile.write(accuracy)