#Author - Ansh Thayil
#Advent of Code 2015 day 11 - Corporate Policy

file = open("inputday11.txt")
string = file.read()
string = string.strip('\n')


def check(array):
    for i in range(len(array)-1,-1,-1):
        if array[i] == "{":
            array[i] = "a"
            array[i-1] = chr(ord(array[i-1])+ 1)
    return array

def increment(string):
    array = list(string)
    end = len(string) - 1
    array[end] = chr(ord(array[end]) + 1)
    check(array)
    string = "".join(array)
    return string

def abc(string):
    for i in range(0,len(string)-2):
        if ord(string[i+1]) == (ord(string[i]) + 1) and ord(string[i+2]) == (ord(string[i]) + 2):
            return True
    return False

def iol(string):
    if 'i' in string or 'o' in string or 'l' in string:
        return False
    return True

def aa(string):
    count = 0
    for j in range(0,len(string) - 1):
        if string[j] == string[j+1]:
            pair1 = string[j] + string[j+1]
            for i in range(j + 2, len(string) -1):
                if string[i] == string[i+1]:
                    pair2 = string[i] + string[i+1]
                    if pair1 != pair2:
                        return True
    return False

def Valid(string):
    if abc(string) and iol(string) and aa(string):
        return True
    return False

while not Valid(string):
    string = increment(string)

print(string)

string = increment(string)

while not Valid(string):
    string = increment(string)

print(string)
