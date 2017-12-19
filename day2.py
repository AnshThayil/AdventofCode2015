#author - Ansh Thayil
#Advent of Code 2015 Day 2 - I Was Told There Would Be No Math

file = open('inputday2.txt')
text = file.read()
num = []
dimens = []
totalarea = 0
totalribbon = 0

for i in text:

    if i == 'x' or i == '\n':
        number = int(''.join(num))
        num = []
        dimens.append(number)

    else:
        num.append(i)

for l in range(0, len(dimens),3):

    a1 = dimens[l] * dimens[l + 1]
    a2 = dimens[l + 1] * dimens[l + 2]
    a3 = dimens[l] * dimens[l + 2]

    if a1 < a2:
        a4 = a1
    else:
        a4 = a2

    if a4 > a3:
        a4 = a3

    area = (2 * a1) + (2 * a2) + (2 * a3) + a4

    p1 = 2 * (dimens[l] + dimens[l + 1])
    p2 = 2 * (dimens[l + 1] + dimens[l + 2])
    p3 = 2 * (dimens[l] + dimens[l + 2])
    ribbonslack = dimens[l] * dimens[l + 1] * dimens[l + 2]

    if p1 < p2:
        ribbon = p1
    else:
        ribbon = p2

    if ribbon > p3:
        ribbon = p3

    totalarea += area
    totalribbon += (ribbon + ribbonslack)

print(totalarea)
print(totalribbon)
