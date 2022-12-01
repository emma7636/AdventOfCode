numberArray = []
plateArray = []
with open('2021/Day 4 - WinBingo/numberfile.txt', 'rt') as f:
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

winningPlate = []
spentNumbers = []
exit = False
for number in numberArray:
    if (exit):
        break
    spentNumbers.append(number)
    for plate in plateArray:
        for row in plate:
            if all([row[0] in spentNumbers, row[1] in spentNumbers, row[2] in spentNumbers, row[3] in spentNumbers, row[4] in spentNumbers]):
                winningPlate = plate
                exit = True
        j = 0
        while(j < 5):
            if all([plate[0][j] in spentNumbers, plate[1][j] in spentNumbers, plate[2][j] in spentNumbers, plate[3][j] in spentNumbers, plate[4][j] in spentNumbers]):
                winningPlate = plate
                exit = True
            j += 1

print(winningPlate)

i = 0
sum = 0
while (i < 5):
    j = 0
    while (j < 5):
        if winningPlate[i][j] not in spentNumbers:
            sum += winningPlate[i][j]
        j += 1
    i += 1

print(sum * spentNumbers[len(spentNumbers) - 1])