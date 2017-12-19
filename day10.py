#Author - Ansh Thayil
#Advent of Code 2015 Day 10 - Elves Look, Elves Say

file = open("inputday10.txt")
string = file.read()

count = 1
answer = []
n = input("40 or 50?\n")
for x in range(0,int(n)):
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            count += 1
        elif string[i] != string[i-1] or string[i] == "\n":
            answer.append(str(count))
            answer.append(string[i-1])
            count = 1
    answer.append("\n")
    string = "".join(answer)
    answer = []

print(len(string)-1)
