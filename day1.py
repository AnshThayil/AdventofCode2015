#author - Ansh Thayil
#Advent of Code 2015 Day 1 - Not Quite Lisp

floor = 0
basement = []

def up(x):
    x += 1
    return x

def down(x):
    x -= 1
    return x

inp = open('inputday1.txt')
text = inp.read()

for i in range(len(text)):

    if text[i] == "(":
        floor = up(floor)

        if floor == -1:
            basement.append(i)

    elif text[i] == ")":
        floor = down(floor)

        if floor == -1:
            basement.append(i)

print (floor)
print (basement[0] + 1)
