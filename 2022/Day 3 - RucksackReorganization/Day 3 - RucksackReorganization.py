backpacks = []
with open('2022/Day 3 - RucksackReorganization/numberfile.txt') as f:
    for line in f.readlines():
        backpacks.append(line)

totalSum = 0
for backpack in backpacks:
    compartment1 = backpack[slice(0, len(backpack) // 2)]
    compartment2 = backpack[slice(len(backpack) // 2, len(backpack))]

    temp = []
    for item in compartment1:
        if item in temp:
            continue
        if item in compartment2:
            value = ord(item)-96
            if value < 0:
                value += 32+26
            totalSum += value

            temp.append(item)
            continue

print(totalSum)