import random
import uuid
zh = open('/home/thinkerpal/Desktop/project/data/act-multiun/cleaned.zh', 'r')
alpha = open('/home/thinkerpal/Desktop/project/data/act-multiun/fullnoalpha.zh', 'w+')
dict = {}
def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
# Convert UUID format to a Python string.
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]
counter = 0
for line in zh:
    line = line.strip()
    newline = ""
    for word in line:
        if word == " ":
            newline += " "
        else:
            if word in dict:
                newline += dict[word]
            else:
                tmp = my_random_string()
                dict[word] = tmp
                newline += tmp
    alpha.write(newline + "\n")
    counter += 1
    if counter % 50000 == 0:
        print(counter)




