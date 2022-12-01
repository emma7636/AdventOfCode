import numpy as numpy

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

def is_in(x, nested):
    result = False
    if not isinstance(nested, (tuple, list)):         
        return result
    for item in nested:
        if x == item:
            result = True
        else:
            result = result or is_in(x, item)
        if result:
            return True
    return result

losingPlates = []
spentNumbers = []
exit = False
for number in numberArray:
    spentNumbers.append(number)
    for plate in plateArray:
        for row in plate:
            if all([row[0] in spentNumbers, row[1] in spentNumbers, row[2] in spentNumbers, row[3] in spentNumbers, row[4] in spentNumbers]):
                if plate in plateArray:
                    if(len(losingPlates) > 0):
                        losingPlates.append(plate)
                        plateArray.remove(plate)
                    else:
                        losingPlates.append(plate)
                        plateArray.remove(plate)
            
            j = 0
            while(j < 5):
                if all([plate[0][j] in spentNumbers, plate[1][j] in spentNumbers, plate[2][j] in spentNumbers, plate[3][j] in spentNumbers, plate[4][j] in spentNumbers]):
                    if plate in plateArray:
                        if (len(losingPlates) > 0):
                            losingPlates.append(plate)
                            plateArray.remove(plate)
                        else:
                            losingPlates.append(plate)
                            plateArray.remove(plate)
                j += 1
    if len(plateArray) == 0:
        break

print(losingPlates[len(losingPlates) - 1])

i = 0
sum = 0
while (i < 5):
    j = 0
    while (j < 5):
        if losingPlates[len(losingPlates) - 1][i][j] not in spentNumbers:
            sum += losingPlates[len(losingPlates) - 1][i][j]
        j += 1
    i += 1

print(sum * spentNumbers[len(spentNumbers) - 1])