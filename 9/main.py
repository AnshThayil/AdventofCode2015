#Author - Ansh Thayil
#Advent of Code 2015 Day 9 - All in a single night.

file = open("inputday9.txt")
text = file.readlines()

from itertools import permutations

distances = dict()

for line in text:
    temp = line.split()
    start = temp[0]
    end = temp[2]
    dist = int(temp[4])

    if start in distances.keys():
        distances[start].append((end,dist))
    else:
        distances[start] = [(end,dist)]

    if end in distances.keys():
        distances[end].append((start,dist))
    else:
        distances[end] = [(start,dist)]

paths = permutations(distances.keys())

def distanceofpath(path):
    distance = 0
    path = list(path)

    while len(path) > 1:

        destinations = distances[path.pop(0)]

        for (d,dist) in destinations:
            if d == path[0]:
                distance += dist
                break
    return distance

minimumpath = []
minimumdist = 100000000000000000000000000000000000000000000000000000000000000000000000000000000
maximumpath = []
maximumdist = 0

for path in paths:
    if distanceofpath(path) < minimumdist:
        minimumpath = path
        minimumdist = distanceofpath(path)
    if distanceofpath(path) >maximumdist:
        maximumpath = path
        maximumdist = distanceofpath(path)

print(minimumpath)
print(minimumdist)
print(maximumpath)
print(maximumdist)
