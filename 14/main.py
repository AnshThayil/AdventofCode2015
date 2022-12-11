#Author - Ansh Thayil
#Advent of Code 2015 Day 14 - Reindeer Olympics

file = open("inputday14.txt")
lines = file.readlines()
speeds = dict()
for line in lines:
    line = line.split(" ")
    speeds[line[0]] = [int(line[3]),int(line[6]),int(line[13])]

test = [14,10,127]
def distcovered(timepassed,test):
    time = 0
    count = 0
    while time < timepassed:
        for i in range(0,test[1]):
            if time < timepassed:
                time += 1
                count += 1
        time += test[2]
    dist = count * test[0]
    return dist

position_at_2503 = []
timepassed = 2503
for deer in speeds.keys():
    position_at_2503.append(distcovered(timepassed,speeds[deer]))

fastestspeed = 0
for dist in position_at_2503:
    if dist > fastestspeed:
        fastestspeed = dist

print(fastestspeed)

deers = dict()
for i in speeds.keys():
    deers[i] = [0,0]
for t in range(1,2504):
    for i in deers.keys():
        deers[i][0] = distcovered(t,speeds[i])
    max = 0
    for i in deers.keys():
        if deers[i][0] > max:
            max = deers[i][0]
    for i in deers.keys():
        if max == deers[i][0]:
            deers[i][1] += 1
maxpoints = 0
for i in speeds.keys():
    if maxpoints < deers[i][1]:
        maxpoints = deers[i][1]
print(maxpoints)
