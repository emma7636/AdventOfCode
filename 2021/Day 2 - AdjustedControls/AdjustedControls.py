tupleArray = []
with open('2021/Day 2 - Controls/numberfile.txt', 'rt') as f:
    for line in f.readlines():
        var = line.split()
        tupleArray.append((var[0], int(var[1])))

hozPos = 0
depth = 0
aim = 0
for command in tupleArray:
    match command[0]:
        case 'forward':
            hozPos += command[1]
            depth += aim * command[1]
        case 'down':
            aim += command[1]
        case 'up':
            aim -= command[1]

print(hozPos * depth)