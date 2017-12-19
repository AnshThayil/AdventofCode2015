#author - Ansh Thayil
#Advent of Code 2015 Day 3 - Perfectly Spherical Houses in a Vacuum

x = 0
y = 0
xlist =[0]
ylist = [0]
coords = []

def removeduplicates(list):
    workablelist = list
    list_without_duplicates = []
    for i in range(len(list)):
        for j in range(i + 1,len(list)):
            if list[i] == list[j]:
                workablelist[j] = '*'
    for i in range(len(list)):
        if workablelist[i] != "*":
            list_without_duplicates.append(list[i])
    return list_without_duplicates

file = open("inputday3.txt")
text = file.read()

for i in text:

    if i == "^":
        y += 1
        xlist.append(x)
        ylist.append(y)

    elif i == "v":
        y -= 1
        xlist.append(x)
        ylist.append(y)

    elif i == ">":
        x += 1
        xlist.append(x)
        ylist.append(y)

    elif i == "<":
        x -= 1
        xlist.append(x)
        ylist.append(y)

for i in range(len(xlist)):
    coord = []
    coord.append(xlist[i])
    coord.append(ylist[i])
    coords.append(coord)

coords_wo_duplicates = removeduplicates(coords)

xlist = [0]
ylist = [0]
x1 = 0
y1 = 0
x2 = 0
y2 = 0
boo = 0
part2coords = []

for i in text:

    if boo == 0:

        if i == "^":
            y1 += 1
            xlist.append(x1)
            ylist.append(y1)

        elif i == "v":
            y1 -= 1
            xlist.append(x1)
            ylist.append(y1)

        elif i == ">":
            x1 += 1
            xlist.append(x1)
            ylist.append(y1)

        elif i == "<":
            x1 -= 1
            xlist.append(x1)
            ylist.append(y1)

        boo = 1

    elif boo == 1:

        if i == "^":
            y2 += 1
            xlist.append(x2)
            ylist.append(y2)

        elif i == "v":
            y2 -= 1
            xlist.append(x2)
            ylist.append(y2)

        elif i == ">":
            x2 += 1
            xlist.append(x2)
            ylist.append(y2)

        elif i == "<":
            x2 -= 1
            xlist.append(x2)
            ylist.append(y2)

        boo = 0

for i in range(len(xlist)):
    coord = []
    coord.append(xlist[i])
    coord.append(ylist[i])
    part2coords.append(coord)

part2_coords_wo_duplicates = removeduplicates(part2coords)

print(len(coords_wo_duplicates))
print(len(part2_coords_wo_duplicates))
