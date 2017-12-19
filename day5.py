#author - Ansh Thayil
#Advent of Code 2015 Day 5 - Doesn't He Have Intern-Elves For This?

file = open("inputday5.txt")
text = file.read()
string = []
strings = []
NiceStringsOld = []
NiceStringsNew = []

def checkvowel(string):
    count = 0
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count += 1
    if count >= 3:
        return True
    return False

def checkdouble(string):
    count = 0
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def checkstring(string):
    count = 0
    for i in range(0,len(string)-1):
        if string[i] == "a" and string[i + 1] == "b":
            return False
        elif string[i] == "c" and string[i + 1] == "d":
            return False
        elif string[i] == "p" and string[i + 1] == "q":
            return False
        elif string[i] == "x" and string[i + 1] == "y":
            return False
    return True

def checkpalindrome(string):
    count = 0
    for i in range(1,len(string) - 1):
        if string[i - 1] == string[i + 1]:
            return True
    return False

def checkdoublepair(string):
    count = 0
    for j in range(0,len(string) - 1):
        pair1 = string[j] + string[j+1]
        for i in range(j + 2, len(string) -1):
            pair2 = string[i] + string[i + 1]
            if pair1 == pair2:
                return True
    return False

def NaughtyOrNiceNew(string):
    if checkpalindrome(string) and checkdoublepair(string):
        return True
    return False

def NaughtyOrNiceOld(string):
    if checkvowel(string) and checkdouble(string) and checkstring(string):
        return True
    return False

for i in text:

    if i == "\n":
        strings.append(string)
        string = []
    else:
        string.append(i)

for string in strings:

    if NaughtyOrNiceOld(string):
        NiceStringsOld.append(string)

for string in strings:

    if NaughtyOrNiceNew(string):
        NiceStringsNew.append(string)


print (len(NiceStringsOld))
print(len(NiceStringsNew))
