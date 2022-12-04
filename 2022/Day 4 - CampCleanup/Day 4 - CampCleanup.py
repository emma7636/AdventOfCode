elfPairs = []
with open('2022/Day 4 - CampCleanup/numberfile.txt') as f:
    for line in f.readlines():
        line = line.split('\n')[0]
        elfPairs.append(line.split(','))

totalPairs = 0
for pair in elfPairs:
    allotment1 = pair[0].split('-')
    allotment2 = pair[1].split('-')

    if int(allotment1[0]) >= int(allotment2[0]) and int(allotment1[1]) <= int(allotment2[1]):
        totalPairs += 1
    elif int(allotment1[0]) <= int(allotment2[0]) and int(allotment1[1]) >= int(allotment2[1]):
        totalPairs += 1

print(totalPairs)