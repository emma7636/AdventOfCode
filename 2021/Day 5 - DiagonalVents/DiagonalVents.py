from this import d


positionArray = []
with open('2021/Day 5 - HydrothermalVents/numberfile.txt', 'rt') as f:
    for position in f:
        positionArray.append(position)

ventMap = []
for i in range(1000):
    ventMap.append([0] * 1000)

def extractData(string = ''):
    string = string.strip('\n')
    dataSets = string.split(' -> ')
    dataSet1 = dataSets[0].split(',')
    dataSet2 = dataSets[1].split(',')
    return dataSet1, dataSet2

for positionCollection in positionArray:
    position1, position2 = extractData(positionCollection)
    position1[0] = int(position1[0])
    position1[1] = int(position1[1])
    position2[0] = int(position2[0])
    position2[1] = int(position2[1])

    if position1[0] == position2[0]:
        if position1[1] < position2[1]:
            for i in range(position1[1], position2[1] + 1):
                ventMap[position1[0]][i] += 1
        else:
            for i in range(position2[1], position1[1] + 1):
                ventMap[position1[0]][i] += 1
    elif position1[1] == position2[1]:
        if position1[0] < position2[0]:
            for i in range(position1[0], position2[0] + 1):
                ventMap[i][position1[1]] += 1
        else:
            for i in range(position2[0], position1[0] + 1):
                ventMap[i][position1[1]] += 1

    elif position2[0] - position1[0] == position2[1] - position1[1]:
        if position1[0] < position2[0]:
            for i in range(position2[0] - position1[0] + 1):
                ventMap[position1[0] + i][position1[1] + i] += 1
        else:
            for i in range(position1[0] - position2[0] + 1):
                ventMap[position2[0] + i][position2[1] + i] += 1
    elif position2[0] - position1[0] == (position2[1] - position1[1]) * (-1):
        if position1[0] < position2[0]:
            for i in range(position2[0] - position1[0] + 1):
                ventMap[position1[0] + i][position1[1] - i] += 1
        else:
            for i in range(position1[0] - position2[0] + 1):
                ventMap[position2[0] + i][position2[1] - i] += 1

count = 0
for i in range(len(ventMap)):
    for j in range(len(ventMap[i])):
        if ventMap[i][j] >= 2:
            count += 1

print('There are ' + str(count) + ' points where two or more lines overlap')