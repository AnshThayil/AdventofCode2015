#author - Ansh Thayil
#Advent of Code 2015 Day 6 -  Probably a Fire Hazard

file = open('inputday6.txt')
text = file.read()

def count(board):
    count = 0
    for y in range(0,1000):
        for x in range(0,1000):
            if board[y][x] == 1:
                count += 1
    return count

def newcount(board):
    count = 0
    for y in range(0,1000):
        for x in range(0,1000):
            count += board[x][y]
    return count

def turnon(y1,x1,y2,x2,board):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            board[y][x] = 1

def newturnon(y1,x1,y2,x2,board):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            board[y][x]  += 1

def turnoff(y1,x1,y2,x2,board):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            board[y][x] = 0

def newturnoff(y1,x1,y2,x2,board):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            if board[y][x] != 0:
                board[y][x]  -= 1

def toggle(y1,x1,y2,x2,board):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            if board[y][x] == 0:
                board[y][x] = 1
            elif board[y][x] == 1:
                board[y][x] = 0

def newtoggle(y1,x1,y2,x2,board):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            board[y][x] += 2

def ProcessCommand(string):
    word = []
    array = []
    for i in text:
        if i == "\n" or i == " " or i == ",":
            word = ''.join(word)
            array.append(word)
            word = []
        else:
            word.append(i)
    for i in array:
        if i == 'turn' or i == 'through':
            array.remove(i)
    return array

ProcessedCommands = ProcessCommand(text)

board = [[0 for i in range(0,1000)] for j in range(0,1000)]

for element in range(0,len(ProcessedCommands),5):
    if ProcessedCommands[element] == 'on':
        x1 = int(ProcessedCommands[element + 1])
        y1 = int(ProcessedCommands[element + 2])
        x2 = int(ProcessedCommands[element + 3])
        y2 = int(ProcessedCommands[element + 4])
        turnon(y1,x1,y2,x2,board)
    elif ProcessedCommands[element] == 'off':
        x1 = int(ProcessedCommands[element + 1])
        y1 = int(ProcessedCommands[element + 2])
        x2 = int(ProcessedCommands[element + 3])
        y2 = int(ProcessedCommands[element + 4])
        turnoff(y1,x1,y2,x2,board)
    elif ProcessedCommands[element] == 'toggle':
        x1 = int(ProcessedCommands[element + 1])
        y1 = int(ProcessedCommands[element + 2])
        x2 = int(ProcessedCommands[element + 3])
        y2 = int(ProcessedCommands[element + 4])
        toggle(y1,x1,y2,x2,board)

print(count(board))

board = [[0 for i in range(0,1000)] for j in range(0,1000)]

for element in range(0,len(ProcessedCommands),5):
    if ProcessedCommands[element] == 'on':
        x1 = int(ProcessedCommands[element + 1])
        y1 = int(ProcessedCommands[element + 2])
        x2 = int(ProcessedCommands[element + 3])
        y2 = int(ProcessedCommands[element + 4])
        newturnon(y1,x1,y2,x2,board)
    elif ProcessedCommands[element] == 'off':
        x1 = int(ProcessedCommands[element + 1])
        y1 = int(ProcessedCommands[element + 2])
        x2 = int(ProcessedCommands[element + 3])
        y2 = int(ProcessedCommands[element + 4])
        newturnoff(y1,x1,y2,x2,board)
    elif ProcessedCommands[element] == 'toggle':
        x1 = int(ProcessedCommands[element + 1])
        y1 = int(ProcessedCommands[element + 2])
        x2 = int(ProcessedCommands[element + 3])
        y2 = int(ProcessedCommands[element + 4])
        newtoggle(y1,x1,y2,x2,board)

print(newcount(board))
