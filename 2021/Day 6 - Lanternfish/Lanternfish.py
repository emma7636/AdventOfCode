class Lanternfish:
    def __init__(self, timer):
        self.timer = timer

lanternfish = []
with open('2021/Day 6 - Lanternfish/numberfile.txt', 'rt') as f:
    lines = f.readline().split(',')
    for line in lines:
        lanternfish.append(Lanternfish(int(line)))

for i in range(80):
    tempArr = []
    for fish in lanternfish:
        if fish.timer == 0:
            tempArr.append(Lanternfish(8))
            fish.timer = 6
        else:
            fish.timer -= 1
    lanternfish.extend(tempArr)

print(len(lanternfish))