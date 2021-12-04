numberArray = []
plateArray = []
with open('Day 4 - WinBingo/numberfile.txt', 'rt') as f:
    for number in f.readline().split(','):
                numberArray.append(int(number))
    
    i = 0
    f.readline()
    currentBoard = [[], [], [], [], []]
    for line in f.readlines():
        if (line == '\n'):
            plateArray.append(currentBoard)
            i = 0
            currentBoard = [[], [], [], [], []]
        else:
            for number in line.split():
                currentBoard[i].append(int(number))
            i += 1
    plateArray.append(currentBoard)