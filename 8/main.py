#Author - Ansh Thayil
#Advent of Code 2015 Day 8 - Matchsticks

file = open('inputday8.txt')
lines = file.readlines()

allcchars = []
memorychars = []
escapedchars = []
for item in lines:
    item = item.strip()
    ac.append(len(item))
    mc.append(len(eval(item)))
    ec.append(item.count("\\") + item.count("\"") + 2 + len(item))

print (sum(ac) - sum(mc))

print (sum(ec) - sum(ac))
