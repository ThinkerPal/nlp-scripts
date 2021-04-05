import os
import jieba

# Creates a list of already used files
PROJECT_ROOT = "/project/data/multiun"
FILES_ARCHIVE = []
multiUN_ENGLISH = open(PROJECT_ROOT + "/results/multiUN.en-zh.en", 'w+', encoding='utf-8')
multiUN_CHINESE = open(PROJECT_ROOT + "/results/multiUN.en-zh.zh", 'w+', encoding='utf-8')
log = open('log', 'w+')

for i in range(2000, 2010):
    FOLDER_ROOT = PROJECT_ROOT + "/" + str(i)
    print(i)
    print(FOLDER_ROOT)
    if not os.path.exists(FOLDER_ROOT):
        break
    else:
        currentDIR = os.listdir(FOLDER_ROOT)
        for fullFileName in currentDIR:
            uniqueFileName = fullFileName[:-7] # Uses unique file name to add the file once
            if uniqueFileName in FILES_ARCHIVE:
                print("File exists, skipping")
                continue
            else:
                print(uniqueFileName)
                FILES_ARCHIVE.append(uniqueFileName)

                en_og = open(FOLDER_ROOT + "/" + uniqueFileName + "_en.snt", 'r', encoding='utf-8')
                zh_og = open(FOLDER_ROOT + "/" + uniqueFileName + "_zh.snt", 'r', encoding='utf-8')
                enEdit = []
                zhEdit = []
                # print(en_og)
                # print(zh_og)
              
                for line in en_og:
                    if line != "\n" and len(line)>10:
                        line = line.strip()
                        enEdit.append(line)
                for line in zh_og:
                    if line != "\n" and len(line)>7:
                        line = line.strip()
                        zhEdit.append(line)
                # if len(enEdit) != len(zhEdit):
                #     print("Not equal")
                #     print(len(enEdit))
                #     print(len(zhEdit))
                #     break;
                else:
                    # print(len(enEdit))
                    # print(len(zhEdit))

                    for i in enEdit:
                        # print(i)
                        multiUN_ENGLISH.write(i + "\n")
                        newline = jieba.lcut(i)
                        newStringLine = ""
                        for word in newline:
                            if newline.index(word) != len(newline):
                                newStringLine += word + " "
                            else:
                                newStringLine += word
                        multiUN_CHINESE.write(newStringLine + "\n")


multiUN_ENGLISH.close()
multiUN_CHINESE.close()
log.writelines(FILES_ARCHIVE)     