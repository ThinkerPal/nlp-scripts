#combiningtextfiles.py
import io
from sklearn.model_selection import train_test_split

x = []
y = []
with io.open('Europarl.de-en.de','r',encoding = 'utf-8') as file1:
    with io.open('Europarl.de-en.en','r',encoding = 'utf-8') as file2:    
        with io.open('train.txt','w+',encoding = 'utf-8') as file3:  
            with io.open('test.txt','w+',encoding = 'utf-8') as file4:
                for line in file1:
                    line = line.strip()
                    x.append(line)
                for line in file2:
                    line = line.strip()
                    y.append(line)
                x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
                
                
                for i in range(len(x_train)):
                    d = x_train[i] + ' ||| ' + y_train[i] + '\n'
                    file3.write(d)
                    
                for i in range(len(x_test)):
                    d = x_test[i] + ' ||| ' + y_test[i] + '\n'
                    file4.write(d)


"""import io
from sklearn.model_selection import train_test_split

x = []
y = []
with io.open('Europarl.de-en.de','r',encoding = 'utf-8') as file1:
    with io.open('Europarl.de-en.en','r',encoding = 'utf-8') as file2:    
        with io.open('resultant2.txt','w+',encoding = 'utf-8') as file3:  
                for line in file1:
                    line = line.strip()
                    x.append(line)
                for line in file2:
                    line = line.strip()
                    y.append(line)
                x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
                
                
                for i in range(len(x)):
                    d = y[i] + ' ||| ' + x[i] + '\n'
                    file3.write(d)"""
            

"""from sklearn.model_selection import train_test_split 
file1 = io.open('Europarl.de-en.de','r',encoding = 'utf-8')
file2 = io.open('Europarl.de-en.en','r',encoding = 'utf-8')
x= []
y= []
for line in file1:
    line=line.strip()
    x.append(line)
for line in file2:
    line=line.strip()
    y.append(line)    
x, x_test, y, y_test = train_test_split (x_train,labels, test_size=0.2, train_size=0.8 )
x_train, x_cv, y_train, y_cv = train_test_split(x,y,test_size = 0.25, train_size =0.75)"""
            

