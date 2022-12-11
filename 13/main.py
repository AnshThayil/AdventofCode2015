#Author - Ansh Thayil
#Advent of Code 2015 Day 13 - Knights of the Dinner Table

file = open("inputday13.txt")
text = file.read()
text = text.split('.\n')
text.pop()

from itertools import permutations

dic = dict()


for line in text:
    temp = line.split(" ")
    person = temp[0]
    if temp[2] == "gain":
        points = int(temp[3])
    elif temp[2] == "lose":
        points = int(temp[3]) * -1
    adjacent = temp[10]

    if person in dic.keys():
        dic[person].append((adjacent,points))
    else:
        dic[person] = [(adjacent,points)]

arrangements = permutations(dic.keys())

def potentialhappiness(arrangement):
    halfhappy = 0
    happy = 0
    arrangement = list(arrangement)
    start = arrangement[0]
    reverse = list(reversed(arrangement))
    end = reverse[0]

    for i in range(1,len(arrangement)):
        for (j, points) in dic[arrangement[i]]:
            if j == arrangement[i-1]:
                happy += points
    for i in range(1,len(arrangement)):
        for (j, points) in dic[reverse[i]]:
            if j == reverse[i-1]:
                happy += points

    for (j,points) in dic[end]:
        if j == start:
            happy += points
    for (j,points) in dic[start]:
        if j == end:
            happy += points

    return happy


maxhappy = 0
maxhappyarrangement = []

for arrangement in arrangements:
    if potentialhappiness(arrangement) > maxhappy:
        maxhappyarrangement = arrangement
        maxhappy = potentialhappiness(arrangement)
print(maxhappy)
print(maxhappyarrangement)

other = dic.keys()
dic["Ansh"] = []

for x in other:
    dic[x].append(("Ansh", 0))
    dic["Ansh"].append((x,0))

arrangements = permutations(dic.keys())

maxhappy = 0
maxhappyarrangement = []

for arrangement in arrangements:
    if potentialhappiness(arrangement) > maxhappy:
        maxhappyarrangement = arrangement
        maxhappy = potentialhappiness(arrangement)
print(maxhappy)
print(maxhappyarrangement)
