train = open('/home/thinkerpal/Desktop/project/data/europarl/results/train_1.en', 'r')
test = open('/home/thinkerpal/Desktop/project/data/europarl/results/test_1.en', 'r')
wdict = []
count = 0
for line in train:
    count += 1
    line = line.strip()
    for word in line:
        if not word in wdict:
            # print("unique word")
            wdict.append(str(word))
            # count += 1
            # print(len(word))
            

for line in test:
    count += 1
    line = line.strip()
    for word in line:
        if not word in wdict:
            # print("unique word")
            wdict.append(str(word))
            

print(len(wdict))
# print(wdict)
print(count)