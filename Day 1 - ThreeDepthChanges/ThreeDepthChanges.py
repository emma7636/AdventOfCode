binaryArray = []
with open('Day 1 - ThreeDepthChanges/numberfile.txt', 'rb') as f:
    binaryArray = list(f)

intArray = []
for binary in binaryArray:
    intArray.append(int(binary))

int1 = 0
int2 = 0
int3 = 0
increaseCount = 0
for int in intArray:
    if (int1 == 0):
        int1 = int
    elif (int2 == 0):
        int2 = int1
        int1 = int
    elif (int3 == 0):
        int3 = int2
        int2 = int1
        int1 = int
    else:
        prevInt = int1 + int2 + int3
        int3 = int2
        int2 = int1
        int1 = int
        currentInt = int1 + int2 + int3

        changes = ''
        if (currentInt - prevInt > 0):
            changes = ' (Increased)'
            increaseCount += 1
        else:
            changes = ' (Decreased)'
        print(str(currentInt) + changes)

print('Depth increased ' + str(increaseCount) + ' times.')