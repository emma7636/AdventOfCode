backpacks = []
with open('2022/Day 3 - IdentificationBadges/numberfile.txt') as f:
    for line in f.readlines():
        backpacks.append(line.split('\n')[0])

totalSum = 0
for i in range(0, len(backpacks), 3):
    backpack1 = backpacks[i]
    backpack2 = backpacks[i+1]
    backpack3 = backpacks[i+2]

    temp = []
    for item in backpack1:
        if item in temp:
            continue
        if item in backpack2 and item in backpack3:
            value = ord(item)-96
            if value < 0:
                value += 32+26
            totalSum += value

            temp.append(item)

print(totalSum)