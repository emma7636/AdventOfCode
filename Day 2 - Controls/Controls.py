tupleArray = []
with open('Day 2 - Controls/numberfile.txt', 'rt') as f:
    for line in f.readlines():
        var = line.split()
        tupleArray.append((var[0], int(var[1])))

posX = 0
posY = 0
for command in tupleArray:
    match command[0]:
        case 'forward':
            posX += command[1]
        case 'down':
            posY += command[1]
        case 'up':
            posY -= command[1]

print(posX * posY)