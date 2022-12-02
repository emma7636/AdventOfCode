strat = []
with open('2022/Day 2 - RockPaperScissors/numberfile.txt', 'rt') as f:
    for line in f.readlines():
        data = line.split(' ')
        strat.append((data[0], data[1].split('\n')[0]))

pointsLUT = {'X': 1, 'Y': 2, 'Z': 3}
winnerLUT = {'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}

points = 0
for line in strat:
    points += pointsLUT[line[1]]
    points += winnerLUT[line[0] + line[1]]

print(points)