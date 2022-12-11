#Author - Ansh Thayil
#Advent of Code 2015 - No Such thing As Too Much

file = open('inputday17.txt')
text = file.readlines()

import itertools

tubs = []
for line in text:
    tubs.append(int(line))

count = 0

for i in range(0,len(tubs)+1):
    for subtub in itertools.combinations(tubs,i):
        if sum(list(subtub)) == 150:
            count += 1

print(count)


count = dict()

for i in range(0,len(tubs)+1):
    for subtub in itertools.combinations(tubs,i):
        if sum(list(subtub)) == 150:
            length = len(list(subtub))
            if length not in count.keys():
                count[length] = 1
            else:
                count[length] += 1

print(count[min(count.keys())])
