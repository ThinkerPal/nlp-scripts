# split-train.py
import io
from sklearn.model_selection import train_test_split

x = []
y = []
with io.open('/project/data/europarl/results/test_5.en','r',encoding = 'utf-8') as file1: 
    with io.open('/project/data/europarl/results/test_5.de','r',encoding = 'utf-8') as file3:  
        with io.open('/project/data/europarl/results/test_5.reversed','w+',encoding = 'utf-8') as file4:
            for line in file1:
                line = line.strip()
                x.append(line)
            for line in file3:
                line = line.strip()
                y.append(line)
           
            for i in range(len(y)):
                line = x[i] + " ||| " + y[i] + " " + "\n"
                file4.write(line)
            # for i in range(len(x_train)):
            #     d = x_train[i] + ' ||| ' + y_train[i] + '\n'
            #     file3.write(d)
                
            # for i in range(len(x_test)):
            #     d = x_test[i] + ' ||| ' + y_test[i] + '\n'
            #     file4.write(d)
