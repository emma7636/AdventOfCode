strat = []
with open('2022/Day 2 - RockPaperScissors/numberfile.txt', 'rt') as f:
    for line in f.readlines():
        data = line.split(' ')
        strat.append((data[0], data[1].split('\n')[0]))

stratLUT = {'AX': 'C', 'AY': 'A', 'AZ': 'B', 'BX': 'A', 'BY': 'B', 'BZ': 'C', 'CX': 'B', 'CY': 'C', 'CZ': 'A'}
pointsLUT = {'A': 1, 'B': 2, 'C': 3}
winnerLUT = {'AA': 3, 'AB': 6, 'AC': 0, 'BA': 0, 'BB': 3, 'BC': 6, 'CA': 6, 'CB': 0, 'CC': 3}

points = 0
for line in strat:
    answer = stratLUT[line[0] + line[1]]
    points += pointsLUT[answer] + winnerLUT[line[0] + answer]

print(points)