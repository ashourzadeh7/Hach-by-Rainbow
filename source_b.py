import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    l = list()
    d = OrderedDict()
    with open (input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            l.append(row)
        for i in range(1000,10000):
            s = str(i)
            h = hashlib.sha256(s.encode()).hexdigest()
            d[h] = s
    for j in range(len(l)):
        if l[j][1] in d:
            l[j].append(d[l[j][1]])
    f = open(output_file_name,'w')
    for i in range(len(l)):
        f.write(l[i][0]+','+l[i][2]+'\n')
    f.close()

hash_password_hack('hash_inputs.csv','task.csv')