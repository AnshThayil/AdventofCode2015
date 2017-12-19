file = open("inputday16.txt")
text = file.readlines()

SueForReal = {'children':3,
              'cats':7,
              'samoyeds':2,
              'pomeranians':3,
              'akitas':0,
              'vizslas':0,
              'goldfish':5,
              'trees':3,
              'cars':2,
              'perfumes':1
              }

for line in text:
    temp = line.split(",")
    (SueNum,feature, val) = temp[0].split(":")
    temp[0] = feature + ":" + val
    match = True

    for i in range(3):
        (key,val) = temp[i].split(":")
        val = int(val)
        key = key.strip()

        if key in SueForReal.keys():
            if SueForReal[key] != val:
                match = False
    if match == True:
        print(SueNum)


for line in text:
    temp = line.split(",")
    (SueNum,feature, val) = temp[0].split(":")
    temp[0] = feature + ":" + val
    match = True

    for i in range(3):
        (key,val) = temp[i].split(":")
        val = int(val)
        key = key.strip()

        if key in SueForReal.keys():
            if key == "cats" or key == "trees":
                if not val > SueForReal[key]:
                    match = False

            elif key == "pomeranians" or key == "goldfish":
                if not val < SueForReal[key]:
                    match = False

            elif SueForReal[key] != val:
                match = False
    if match == True:
        print(SueNum)
