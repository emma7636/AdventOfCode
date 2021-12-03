binaryArray = []
with open('Day 1 - DepthChanges/numberfile.txt', 'rb') as f:
    binaryArray = list(f)

intArray = []
for binary in binaryArray:
    intArray.append(int(binary))

prevInt = 0
increaseCount = 0
for int in intArray:
    if (prevInt == 0):
        prevInt = int
    else:
        changes = ''
        if (int - prevInt > 0):
            changes = ' (Increased)'
            increaseCount += 1
        else:
            changes = ' (Decreased)'
        print(str(int) + changes)
        prevInt = int

print('Depth increased ' + str(increaseCount) + ' times.')