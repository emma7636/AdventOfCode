class Lanternfish:
    def __init__(self, timer, count):
        self.timer = timer
        self.count = count

lanternfish = []
with open('2021/Day 6 - Lanternfish/numberfile.txt', 'rt') as f:
    tempArr = []
    lines = f.readline().split(',')
    for line in lines:
        tempArr.append(int(line))
    for i in range(9):
        lanternfish.append(Lanternfish(i, tempArr.count(i)))

for i in range(256):
    newLanternfish = 0
    for fish in lanternfish:
        if fish.timer == 0:
            newLanternfish += fish.count
            fish.timer = 6
        else:
            fish.timer -= 1
    lanternfish.append(Lanternfish(8, newLanternfish))
    print(i)

count = 0
for fish in lanternfish:
    count += fish.count
print(count)