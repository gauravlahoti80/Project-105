import math
import csv
from os import read

from numpy import square

with open("data.csv" , newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

#removing the header
file_data.pop(0)
data = file_data[1]

def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total+=int(x)
    mean = total/n
    return mean

print(mean)

#squaring and getting the values
squared_list = []
for num in data:
    a = int(num) - mean(data)
    a ** 2
    squared_list.append(a)

#getting sum
sum = 0
for i in squared_list:
    sum+=i

#dividing the sum by total values
result = sum/(len(data)-1)
print(result)
#getting the standard deviation
std = math.sqrt(result)

print(std)