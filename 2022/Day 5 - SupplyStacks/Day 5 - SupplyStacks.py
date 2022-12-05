from collections import deque

crateStacks = []
moveLines = []

def createCrateStacks(crateLines):
    crateStacks = []
    for i in range(0, 36, 4):
        tempArray = []
        for line in crateLines:
            if line[i+1] == ' ':
                continue
            tempArray.append(line[i+1])
        tempArray.reverse()
        crateStacks.append(deque(tempArray))
    return crateStacks

with open('2022/Day 5 - SupplyStacks/numberfile.txt', 'rt') as f:
    crateLines = []
    finishedStacks = False
    for line in f.readlines():
        if finishedStacks:
            moveLines.append(line)
            continue

        if line == "\n":
            finishedStacks = True
            crateLines.pop()
            continue
        crateLines.append(line)
    
    crateStacks = createCrateStacks(crateLines)

for line in moveLines:
    split = line.split(' ')
    for i in range(int(split[1])):
        crateStacks[int(split[5].split('\n')[0]) - 1].append(crateStacks[int(split[3]) - 1].pop())

result = ""
for stack in crateStacks:
    result += stack.pop()
print(result)