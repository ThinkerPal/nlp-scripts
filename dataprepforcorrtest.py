RESULTS_ROOT = "/project/data/europarl/results/"
OUTPUT_DIR = "/project/data/europarl/"

SOURCE_DATA = open(RESULTS_ROOT + "test_1.de" , 'r', encoding='utf-8') 
SOURCE_DATA2 = open(RESULTS_ROOT + "train_1.de" , 'r', encoding='utf-8')
TARGET_DATA = open(RESULTS_ROOT + "test_1.en" , 'r', encoding='utf-8')
TARGET_DATA2 = open(RESULTS_ROOT + "train_1.en" , 'r', encoding='utf-8')
SOURCE_NEW = open(OUTPUT_DIR + "Europarlrev.de-en.de " , 'w+', encoding='utf-8') 
TARGET_NEW = open(OUTPUT_DIR + "Europarlrev.de-en.en" , 'w+', encoding='utf-8') 


print("Starting to process source file...")
sourcetest = SOURCE_DATA.readlines()
sourcetrain = SOURCE_DATA2.readlines()
for i in sourcetrain:
    sourcetest.append(i)

for i in sourcetest:
    SOURCE_NEW.write(i)


print("Starting to process target file...")
targettest = TARGET_DATA.readlines()
targettrain = TARGET_DATA2.readlines()
for i in targettrain:
    targettest.append(i)

for i in targettest:
    TARGET_NEW.write(i)

SOURCE_DATA.close()
SOURCE_DATA2.close()
TARGET_DATA.close()
TARGET_DATA2.close()
SOURCE_NEW.close()
TARGET_NEW.close()
print("Completed")
