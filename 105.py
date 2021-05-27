import math
import csv 
with open ('data.csv',newline = '') as f :
    reader = csv.reader(f)
    data = list(reader)
data1 = data[0]
def mean (data1):
    n = len (data1)
    total = 0 
    for x in data1 :
        total = total+int(x)
    mean = total/n
    return mean
list = []
for i in data1 :
    a = int(i) - mean (data1)
    a = a**2
    list.append(a)
sum = 0
for j in list :
    sum = sum + j 
result = sum/(len(data1)-1)
standarddeviation =  math.sqrt(result)
print (standarddeviation)
