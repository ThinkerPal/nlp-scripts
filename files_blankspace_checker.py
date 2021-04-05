#!/usr/bin/python3
import os
ROOT = input("What is the directory to be scanned? ")
filesToRead = os.listdir(ROOT)
writAble = []

for i in range(len(filesToRead)):
    print(filesToRead[i])
    if filesToRead[i][0] == 't' and filesToRead[i][0] != '_': 
        with open (ROOT + "/" + filesToRead[i], 'r', encoding='utf-8') as checking:
            saveFile = open(ROOT + "/_" + filesToRead[i], 'w+', encoding='utf-8')
            
            for line in checking:
                if line == "\n":
                    print("newline found")
                    continue
                elif line == " ":
                    print("Space found")
                    continue
                elif line == " ||| ":
                    print("Empty line in combine file")
                    continue
                else:
                    writAble.append(line)
            saveFile.close()h