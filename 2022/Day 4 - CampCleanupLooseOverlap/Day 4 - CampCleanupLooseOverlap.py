elfPairs = []
with open('2022/Day 4 - CampCleanup/numberfile.txt') as f:
    for line in f.readlines():
        line = line.split('\n')[0]
        elfPairs.append(line.split(','))

totalPairs = 0
for pair in elfPairs:
    allotment1 = [int(x) for x in pair[0].split('-')]
    allotment2 = [int(x) for x in pair[1].split('-')]

    if allotment1[0] >= allotment2[0] and allotment1[1] <= allotment2[1]:
        totalPairs += 1
    elif allotment1[0] <= allotment2[0] and allotment1[1] >= allotment2[1]:
        totalPairs += 1
    elif allotment1[0] <= allotment2[0] and allotment1[1] <= allotment2[1] and allotment1[1] >= allotment2[0] and allotment1[0] <= allotment2[1]:
        totalPairs += 1
    elif allotment1[0] >= allotment2[0] and allotment1[1] >= allotment2[1] and allotment1[1] >= allotment2[0] and allotment1[0] <= allotment2[1]:
        totalPairs += 1

print(totalPairs)